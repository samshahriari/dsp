from models.EEGClassifier import create_classifying_model
import os
from models.model_factory import Model_factory
from models.optimizers import get_optimizer, get_loss_module
from torch.utils.data import DataLoader
from Dataset.EEGdataloader import dataset_class
from models.Series2Vec.S2V_training import *


from utils.utils import load_model


import logging

logger = logging.getLogger('__main__')


def choose_trainer(model, train_loader, test_loader, config, conf_mat, type):
    if config['Model_Type'][0] == 'Series2Vec':
        S_trainer = S2V_S_Trainer(model, train_loader, test_loader, config, print_conf_mat=conf_mat)
    return S_trainer


def pre_training(config, Data):
    logger.info("Creating Distance based Self Supervised model ...")
    model = Model_factory(config, Data)
    optim_class = get_optimizer("RAdam")
    config['optimizer'] = optim_class(model.parameters(), lr=config['lr'], weight_decay=0)
    config['loss_module'] = get_loss_module()
    model.to(config['device'])

    # --------------------------------- Load Data ---------------------------------------------------------------------
    train_dataset = dataset_class(Data['train_data'], Data['train_label'], config)
    val_dataset = dataset_class(Data['val_data'], Data['val_label'], config)
    test_dataset = dataset_class(Data['test_data'], Data['test_label'], config)

    train_loader = DataLoader(dataset=train_dataset, batch_size=config['batch_size'], shuffle=True, pin_memory=True)
    val_loader = DataLoader(dataset=val_dataset, batch_size=config['batch_size'], shuffle=True, pin_memory=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=config['batch_size'], shuffle=False, pin_memory=True)

    # --------------------------------- Self Superviseed Training ------------------------------------------------------
    # Create and train the embedding model
    SS_trainer = S2V_SS_Trainer(model, train_loader, test_loader, config, val_loader, print_conf_mat=False)
    save_path = os.path.join(config['save_dir'], config['problem'] + '_model_{}.pth'.format('last'))
    SS_train_runner(config, model, SS_trainer, save_path)

    # --------------------------------------------- Downstream Task (classification)   ---------------------------------
    # ---------------------- Loading the model and freezing layers except FC layer -------------------------------------
    # here begins fine tuning??
    SS_Encoder, optimizer, start_epoch = load_model(model, save_path, config['optimizer'])  # Loading the model. TODO this should be saved to disk
    SS_Encoder.to(config['device'])
    train_repr, train_labels = S2V_make_representation(SS_Encoder, train_loader)  # this is how the data is embedded

    test_repr, test_labels = S2V_make_representation(SS_Encoder, test_loader)

    create_classifying_model(train_repr, train_labels, test_repr, test_labels, Data['test_subject'])  # TODO this should probably be moved

    return  # best_aggr_metrics_test, all_metrics


def supervised(config, Data):
    # TODO this should be removed
    model = Model_factory(config, Data)
    optim_class = get_optimizer("RAdam")
    config['optimizer'] = optim_class(model.parameters(), lr=config['lr'], weight_decay=0)
    config['loss_module'] = get_loss_module()
    model.to(config['device'])

    # --------------------------------- Load Data -------------------------------------------------------------
    train_dataset = dataset_class(Data['train_data'], Data['train_label'], config)
    val_dataset = dataset_class(Data['val_data'], Data['val_label'], config)
    test_dataset = dataset_class(Data['test_data'], Data['test_label'], config)

    train_loader = DataLoader(dataset=train_dataset, batch_size=config['batch_size'], shuffle=True, pin_memory=True)
    val_loader = DataLoader(dataset=val_dataset, batch_size=config['batch_size'], shuffle=True, pin_memory=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=config['batch_size'], shuffle=True, pin_memory=True)

    S_trainer = choose_trainer(model, train_loader, None, config, False, 'S')
    S_val_evaluator = choose_trainer(model, val_loader, None, config, False, 'S')
    save_path = os.path.join(config['save_dir'], config['problem'] + '_model_{}.pth'.format('last'))

    Strain_runner(config, model, S_trainer, S_val_evaluator, save_path)
    best_model, optimizer, start_epoch = load_model(model, save_path, config['optimizer'])
    best_model.to(config['device'])

    best_test_evaluator = choose_trainer(best_model, test_loader, None, config, True, 'S')
    best_aggr_metrics_test, all_metrics = best_test_evaluator.evaluate(keep_all=True)
    return best_aggr_metrics_test, all_metrics

import os
import numpy as np
import logging
import torch
from sklearn import model_selection
from torch.utils.data import Dataset
import random
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sktime.datasets import load_from_tsfile_to_dataframe


logger = logging.getLogger(__name__)


def load(config):
    # Build data
    Data = {}
    problem = config['data_dir'].split('/')[-1]

    if os.path.exists(config['data_dir'] + '/' + problem + '.npy'):
        logger.info("Loading preprocessed data ...")
        Data_npy = np.load(config['data_dir'] + '/' + problem + '.npy', allow_pickle=True)

        Data['max_len'] = Data_npy.item().get('max_len')
        Data['All_train_data'] = Data_npy.item().get('All_train_data')
        Data['All_train_label'] = Data_npy.item().get('All_train_label')
        Data['train_data'] = Data_npy.item().get('train_data')
        Data['train_label'] = Data_npy.item().get('train_label')
        Data['val_data'] = Data_npy.item().get('val_data')
        Data['val_label'] = Data_npy.item().get('val_label')
        Data['test_data'] = Data_npy.item().get('test_data')
        Data['test_label'] = Data_npy.item().get('test_label')

        logger.info("{} samples will be used for training".format(len(Data['train_label'])))
        logger.info("{} samples will be used for validation".format(len(Data['val_label'])))
        logger.info("{} samples will be used for testing".format(len(Data['test_label'])))

    else:

        logger.info("Loading and preprocessing data ...")
        # get file path
        train_file = config['data_dir'] + "/" + problem + "_TRAIN.ts"
        test_file = config['data_dir'] + "/" + problem + "_TEST.ts"

        # x sparas en dataframe och y sparas i en lista med namngivna labels
        # varje kolumn är en dim
        # varje rad är en tidsserie över alla dimensioner
        # ett element är en tidsserie över en dimension
        #    d1  d2  d3  d4
        # s1 []  []  []  []
        # s2 []  []  []  []
        # s3 []  []  []  []
        # s4 []  []  []  []
        train_df, y_train = load_from_tsfile_to_dataframe(train_file)
        # print(train_df.info())
        # import sys
        # sys.exit(0)
        test_df, y_test = load_from_tsfile_to_dataframe(test_file)

        y_train = LabelEncoder().fit_transform(y_train)
        y_test = LabelEncoder().fit_transform(y_test)

        train_lengths = train_df.applymap(lambda x: len(x)).values
        test_lengths = test_df.applymap(lambda x: len(x)).values
        train_max_seq_len = int(np.max(train_lengths[:, 0]))
        test_max_seq_len = int(np.max(test_lengths[:, 0]))
        max_seq_len = np.max([train_max_seq_len, test_max_seq_len])

        X_train = process_ts_data(train_df, max_seq_len, normalise=False)
        X_test = process_ts_data(test_df, max_seq_len, normalise=False)

        if config['Norm']:
            mean, std = mean_std(X_train)
            mean = np.repeat(mean, max_seq_len).reshape(X_train.shape[1], max_seq_len)
            std = np.repeat(std, max_seq_len).reshape(X_train.shape[1], max_seq_len)
            X_train = mean_std_transform(X_train, mean, std)
            X_test = mean_std_transform(X_test, mean, std)

        Data['max_len'] = max_seq_len
        Data['All_train_data'] = X_train
        Data['All_train_label'] = y_train

        if config['val_ratio'] > 0:
            train_data, train_label, val_data, val_label = split_dataset(X_train, y_train, config['val_ratio'])
        else:
            val_data, val_label = [None, None]

        logger.info("{} samples will be used for training".format(len(train_label)))
        logger.info("{} samples will be used for validation".format(len(val_label)))
        logger.info("{} samples will be used for testing".format(len(y_test)))

        Data['train_data'] = train_data
        Data['train_label'] = train_label
        Data['val_data'] = val_data
        Data['val_label'] = val_label
        Data['test_data'] = X_test
        Data['test_label'] = y_test

        np.save(config['data_dir'] + "/" + problem, Data, allow_pickle=True)

    return Data


def split_dataset(data, label, validation_ratio):
    splitter = model_selection.StratifiedShuffleSplit(n_splits=1, test_size=validation_ratio, random_state=1234)
    train_indices, val_indices = zip(*splitter.split(X=np.zeros(len(label)), y=label))
    train_data = data[train_indices]
    train_label = label[train_indices]
    val_data = data[val_indices]
    val_label = label[val_indices]
    return train_data, train_label, val_data, val_label


def fill_missing(x: np.array, max_len: int, vary_len: str = "suffix-noise", normalise: bool = True):
    if vary_len == "zero":
        if normalise:
            x = StandardScaler().fit_transform(x)
        x = np.nan_to_num(x)
    elif vary_len == 'prefix-suffix-noise':
        for i in range(len(x)):
            series = list()
            for a in x[i, :]:
                if np.isnan(a):
                    break
                series.append(a)
            series = np.array(series)
            seq_len = len(series)
            diff_len = int(0.5 * (max_len - seq_len))

            for j in range(diff_len):
                x[i, j] = random.random() / 1000

            for j in range(diff_len, seq_len):
                x[i, j] = series[j - seq_len]

            for j in range(seq_len, max_len):
                x[i, j] = random.random() / 1000

            if normalise:
                tmp = StandardScaler().fit_transform(x[i].reshape(-1, 1))
                x[i] = tmp[:, 0]
    elif vary_len == 'uniform-scaling':
        for i in range(len(x)):
            series = list()
            for a in x[i, :]:
                if np.isnan(a):
                    break
                series.append(a)
            series = np.array(series)
            seq_len = len(series)

            for j in range(max_len):
                scaling_factor = int(j * seq_len / max_len)
                x[i, j] = series[scaling_factor]
            if normalise:
                tmp = StandardScaler().fit_transform(x[i].reshape(-1, 1))
                x[i] = tmp[:, 0]
    else:
        for i in range(len(x)):
            for j in range(len(x[i])):
                if np.isnan(x[i, j]):
                    x[i, j] = random.random() / 1000

            if normalise:
                tmp = StandardScaler().fit_transform(x[i].reshape(-1, 1))
                x[i] = tmp[:, 0]

    return x


def process_ts_data(x, max_len, vary_len: str = "suffix-noise", normalise: bool = False):
    """
    This is a function to process the data, i.e. convert dataframe to numpy array
    :param X:
    :param normalise:
    :return:
    """
    num_instances, num_dim = x.shape
    columns = x.columns
    # max_len = np.max([len(X[columns[0]][i]) for i in range(num_instances)])
    output = np.zeros((num_instances, num_dim, max_len), dtype=np.float64)
    for i in range(num_dim):
        for j in range(num_instances):
            lengths = len(x[columns[i]][j].values)
            end = min(lengths, max_len)
            output[j, i, :end] = x[columns[i]][j].values
        output[:, i, :] = fill_missing(output[:, i, :], max_len, vary_len, normalise)
    return output


def mean_std(train_data):
    m_len = np.mean(train_data, axis=2)
    mean = np.mean(m_len, axis=0)

    s_len = np.std(train_data, axis=2)
    std = np.max(s_len, axis=0)

    return mean, std


def mean_std_transform(train_data, mean, std):
    return (train_data - mean) / std


def data_loader(config):
    if config['problem'] == 'TUEV':
        Data = tuev_loader(config)
    else:
        Data = load(config)
    return Data


def tuev_loader(config):
    Data = {}
    data_path = config['data_dir'] + '/' + config['problem']
    Data['train_data'] = np.load(data_path + '/' + 'train_data.npy', allow_pickle=True)
    Data['train_label'] = np.load(data_path + '/' + 'train_label.npy', allow_pickle=True)
    Data['val_data'] = np.load(data_path + '/' + 'val_data.npy', allow_pickle=True)
    Data['val_label'] = np.load(data_path + '/' + 'val_label.npy', allow_pickle=True)
    Data['All_train_data'] = np.load(data_path + '/' + 'All_train_data.npy', allow_pickle=True)
    Data['All_train_label'] = np.load(data_path + '/' + 'All_train_label.npy', allow_pickle=True)
    Data['test_data'] = np.load(data_path + '/' + 'test_data.npy', allow_pickle=True)
    Data['test_label'] = np.load(data_path + '/' + 'test_label.npy', allow_pickle=True)
    Data['max_len'] = Data['train_data'].shape[1]

    logger.info("{} samples will be used for self-supervised training".format(len(Data['All_train_label'])))
    logger.info("{} samples will be used for fine tuning ".format(len(Data['train_label'])))
    samples, channels, time_steps = Data['train_data'].shape
    logger.info(
        "Train Data Shape is #{} samples, {} channels, {} time steps ".format(samples, channels, time_steps))
    logger.info("{} samples will be used for validation".format(len(Data['val_label'])))
    logger.info("{} samples will be used for test".format(len(Data['test_label'])))
    return Data


def numpy_loader(config):
    # Build data
    Data = {}
    # Get the current directory path
    problem = config['problem']
    # Read the JSON file and load the data into a dictionary
    data_path = config['data_dir'] + '/' + problem + '/' + problem + '.npy'
    if os.path.exists(data_path):
        logger.info("Loading preprocessed " + problem)
        Data_npy = np.load(data_path, allow_pickle=True)
        if np.any(Data_npy.item().get('val_data')):
            Data['train_data'] = Data_npy.item().get('train_data')
            Data['train_label'] = Data_npy.item().get('train_label')
            Data['val_data'] = Data_npy.item().get('val_data')
            Data['val_label'] = Data_npy.item().get('val_label')
            # Data['All_train_data'] = Data_npy.item().get('All_train_data')
            # Data['All_train_label'] = Data_npy.item().get('All_train_label')
            Data['test_data'] = Data_npy.item().get('test_data')
            Data['test_label'] = Data_npy.item().get('test_label')
            Data['max_len'] = Data['train_data'].shape[1]
        else:
            Data['train_data'], Data['train_label'], Data['val_data'], Data['val_label'] = \
                split_dataset(Data_npy.item().get('train_data'), Data_npy.item().get('train_label'), 0.1)
            Data['All_train_data'] = Data_npy.item().get('train_data')
            Data['All_train_label'] = Data_npy.item().get('train_label')
            Data['test_data'] = Data_npy.item().get('test_data')
            Data['test_label'] = Data_npy.item().get('test_label')
            Data['max_len'] = Data['train_data'].shape[2]

        logger.info("{} samples will be used for training".format(len(Data['train_label'])))
        samples, channels, time_steps = Data['train_data'].shape
        logger.info(
            "Train Data Shape is #{} samples, {} channels, {} time steps ".format(samples, channels, time_steps))
        logger.info("{} samples will be used for testing".format(len(Data['test_label'])))

    return Data


def split_dataset(data, label, validation_ratio):
    splitter = model_selection.StratifiedShuffleSplit(n_splits=1, test_size=validation_ratio, random_state=1234)
    train_indices, val_indices = zip(*splitter.split(X=np.zeros(len(label)), y=label))
    train_data = data[train_indices]
    train_label = label[train_indices]
    val_data = data[val_indices]
    val_label = label[val_indices]
    return train_data, train_label, val_data, val_label


class dataset_class(Dataset):
    def __init__(self, data, label, config):
        super(dataset_class, self).__init__()

        self.model_type = config['Model_Type'][0]
        self.feature = data
        self.labels = label.astype(np.int32)

    def __getitem__(self, ind):
        x = self.feature[ind]
        x = x.astype(np.float32)
        y = self.labels[ind]  # (num_labels,) array

        data = torch.tensor(x)
        label = torch.tensor(y)

        return data, label, ind

    def __len__(self):
        return len(self.labels)

import os
import numpy as np
import logging
import torch
from sklearn import model_selection
from torch.utils.data import Dataset
import random
from sklearn.preprocessing import StandardScaler, LabelEncoder

import pandas as pd
import re
logger = logging.getLogger(__name__)


def convert_to_series(cell):
    formatted_cell = re.sub(r'(?<=\d)\s+(?=-?\d)', ', ', cell.strip())
    cell_as_list = eval(formatted_cell)
    return pd.Series(cell_as_list)


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
        import pandas as pd
        # # x sparas en dataframe och y sparas i en lista med namngivna labels
        # # varje kolumn är en dim
        # # varje rad är en tidsserie över alla dimensioner
        # # ett element är en tidsserie över en dimension
        # #    d1  d2  d3  d4
        # # s1 []  []  []  []
        # # s2 []  []  []  []
        # # s3 []  []  []  []
        # # s4 []  []  []  []

        train_df = pd.read_csv(config['data_dir'] + "/" + "X_train.csv").drop("subject_id", axis=1)
        train_df = train_df.applymap(convert_to_series)
        y_train = pd.read_csv(config['data_dir'] + "/" + "y_train.csv").to_numpy()
        test_df = pd.read_csv(config['data_dir'] + "/" + "X_test.csv").drop("subject_id", axis=1)
        test_df = test_df.applymap(convert_to_series)
        y_test = pd.read_csv(config['data_dir'] + "/" + "y_test.csv").to_numpy()

        y_train = LabelEncoder().fit_transform(y_train)
        y_test = LabelEncoder().fit_transform(y_test)
        train_lengths = train_df.applymap(lambda x: len(x)).values
        test_lengths = test_df.applymap(lambda x: len(x)).values
        train_max_seq_len = int(np.max(train_lengths[:, 0]))
        test_max_seq_len = int(np.max(test_lengths[:, 0]))
        max_seq_len = np.max([train_max_seq_len, test_max_seq_len])

        X_train = process_ts_data(train_df, max_seq_len, normalise=False)
        X_test = process_ts_data(test_df, max_seq_len, normalise=False)

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
            lengths = len(x[columns[i]][j])
            end = min(lengths, max_len)
            output[j, i, :end] = x[columns[i]][j].values
        output[:, i, :] = fill_missing(output[:, i, :], max_len, vary_len, normalise)
    return output


def data_loader(config):
    return load(config)


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

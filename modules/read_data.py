import os
import numpy as np
import pandas as pd


def get_metadata_path():
    actual_path = os.getcwd()
    metadata_path = os.path.join(actual_path + '\data\metadata')
    return metadata_path

def load_metadata(metadata_path):
    train_metadata = pd.read_csv(metadata_path + '\\train.csv')
    test_metadata = pd.read_csv(metadata_path + '\\test.csv')
    return train_metadata, test_metadata

def get_signal_path():
    signal_path = os.getcwd()
    signal_path_train = os.path.join(signal_path + '\data\signals\\train')
    signal_path_test  = os.path.join(signal_path + '\data\signals\\test')
    return signal_path_train, signal_path_test

def load_signal(signal_path):
    dictionary_recordId_signals = {}
    list_signals = []
    files = os.listdir(signal_path)
    for file in files:
        record_id = int(file.split('.')[0])
        file_list = []
        try:
            file_path = os.path.join(signal_path, file)
            FHR, UC = np.genfromtxt(file_path, delimiter=',', skip_header=1, usecols=(1, 2), unpack=True)
            file_list.append(list(range(1800)))
            file_list.append(FHR[-1800:])
            file_list.append(UC[-1800:])
            dictionary_recordId_signals[record_id] = file_list
        except Exception as E:
            print('Error in file ' + file)
        list_signals.append(file_list)
    return dictionary_recordId_signals
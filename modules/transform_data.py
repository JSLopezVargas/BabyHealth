import pandas as pd
pd.options.mode.chained_assignment = None

def columns_to_categorical(dataframe, data_type):
    if data_type == 'Train':
        categorical_columns = ['babyhealth', 'sex', 'diabetes', 'hypertension', 'preeclampsia', 'pyrexia', 'meconium', 'noprogress', 'rectype']
        output_dataframe = dataframe.copy()
        for column in categorical_columns:
            if column == 'babyhealth':
                output_dataframe['babyhealth'] = output_dataframe['babyhealth'].map({0: 'Healthy', 1: 'No Healthy'})
                output_dataframe['babyhealth'] = output_dataframe['babyhealth'].astype('object')
            elif column == 'sex':
                output_dataframe['sex'] = output_dataframe['sex'].map({1: 'F', 2: 'M'})
                output_dataframe['sex'] = output_dataframe['sex'].astype('object')
            elif column == 'rectype':
                output_dataframe['rectype'] = output_dataframe['rectype'].map({1: 'Eco', 2: 'Sca', 12: 'Both'})
                output_dataframe['rectype'] = output_dataframe['rectype'].astype('object')
            else:
                output_dataframe[column] = output_dataframe[column].map({0: False, 1: True})
                output_dataframe[column] = output_dataframe[column].astype('object')
    elif data_type == 'Test':
        categorical_columns = ['sex', 'diabetes', 'hypertension', 'preeclampsia', 'pyrexia', 'meconium', 'noprogress', 'rectype']
        output_dataframe = dataframe.copy()
        for column in categorical_columns:
            if column == 'sex':
                output_dataframe['sex'] = output_dataframe['sex'].map({1: 'F', 2: 'M'})
                output_dataframe['sex'] = output_dataframe['sex'].astype('object')
            elif column == 'rectype':
                output_dataframe['rectype'] = output_dataframe['rectype'].map({1: 'Eco', 2: 'Sca', 12: 'Both'})
                output_dataframe['rectype'] = output_dataframe['rectype'].astype('object')
            else:
                output_dataframe[column] = output_dataframe[column].map({0: False, 1: True})
                output_dataframe[column] = output_dataframe[column].astype('object')
    else:
        print('Error in parameter data_type.')
    return output_dataframe

def get_statistical_measures(Value_list):
    series = pd.Series(Value_list)
    mean = series.mean()
    median = series.median()
    std = series.std()
    min_val = series.min()
    error_in_min = 0
    if min_val == 0: error_in_min = 1
    max_val = series.max()
    return [mean, median, std, min_val, error_in_min, max_val]

def merge_data(metadata, signal):
    metadata = metadata.copy()
    metadata.loc[:, 'signal_values'] = metadata['recordID'].map(signal)
    metadata[['seconds', 'FHR', 'UC']] = pd.DataFrame(metadata['signal_values'].tolist(), index=metadata.index)
    metadata.drop('signal_values', axis=1, inplace=True)
    fhr_stats = metadata['FHR'].apply(get_statistical_measures)
    metadata['mean_fhr'] = fhr_stats.apply(lambda x: x[0])
    metadata['median_fhr'] = fhr_stats.apply(lambda x: x[1])
    metadata['std_fhr'] = fhr_stats.apply(lambda x: x[2])
    metadata['min_val_fhr'] = fhr_stats.apply(lambda x: x[3])
    metadata['error_in_min_fhr'] = fhr_stats.apply(lambda x: x[4])
    metadata['max_val_fhr'] = fhr_stats.apply(lambda x: x[5])
    uc_stats = metadata['UC'].apply(get_statistical_measures)
    metadata['mean_uc'] = uc_stats.apply(lambda x: x[0])
    metadata['median_uc'] = uc_stats.apply(lambda x: x[1])
    metadata['std_uc'] = uc_stats.apply(lambda x: x[2])
    metadata['min_val_uc'] = uc_stats.apply(lambda x: x[3])
    metadata['error_in_min_uc'] = uc_stats.apply(lambda x: x[4])
    metadata['max_val_uc'] = uc_stats.apply(lambda x: x[5])
    metadata.drop(['seconds', 'FHR', 'UC'], axis=1, inplace=True)
    return metadata
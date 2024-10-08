import pandas as pd
import numpy as np
import mne_bids
from mne_bids import BIDSPath, read_raw_bids
import matplotlib.pyplot as plt
import os
import mne
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedGroupKFold

import warnings
warnings.simplefilter("ignore", category=RuntimeWarning)

class CustomDataLoader:
    def __init__(self, parameters):
        self.parameters = parameters

    def load_data(self):
        bids_root = './data/' 
        task = 'eyesclosed'
        datatype = 'eeg'
        suffix = 'eeg'

        # Suppress logs
        mne.set_log_level(False)

        df = []

        for filename in os.listdir(bids_root):
            if filename.startswith("sub"):
                subject_id = filename.replace("sub-", "")
                bids_path = BIDSPath(subject=subject_id, task=task, datatype=datatype, suffix=suffix, extension='.set', root=bids_root, check=False)
                raw = read_raw_bids(bids_path, verbose=False)
                raw.resample(sfreq=self.parameters["sampling_frequency"])
                data = raw.to_data_frame()
                df.append({"subject_id": raw.info['subject_info']['his_id'], "data": data, "Y": raw.info['subject_info']['Group']})

        return df  

    def remove_outliers(self, df):
        print("Removing outliers...")
        #print(f"DF length before removal {len(df)}")
        outliers_ids = ['sub-026', 'sub-044', 'sub-063'] # Remove outliers given information from t-SNE plot 
        df_without_outliers = [x for x in df if x['subject_id'] not in outliers_ids]
        #print(f"DF length after removal {len(df_without_outliers)}")
        return df_without_outliers

    def select_subjects(self, df):
        np.random.seed(self.parameters["random_seed"])

        A_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'A'], self.parameters["num_A"], replace=False)
        F_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'F'], self.parameters["num_F"], replace=False)
        C_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'C'], self.parameters["num_C"], replace=False)

        print(f"A Indicies: {A_indicies}")
        print(f"F Indicies: {F_indicies}")
        print(f"C Indicies: {C_indicies}")

        df = [df[i] for i in A_indicies] + [df[i] for i in F_indicies] + [df[i] for i in C_indicies]
        np.random.shuffle(df)
        return df

    def select_channels(self, df):
        print("Selecting channels...")
        for item in df:
            for channel in item['data'].columns:
                if channel not in self.parameters['channels']:
                    item['data'].drop(channel, axis=1, inplace=True)
                    
        return df

    def trim_df(self, df):
        print("Trimming data...")
        timestep_given_sampling_frequency = df[0]['data']['time'][1]
        datapoints_to_remove_beginning = int((self.parameters['minutes_to_remove_beginning'] * 60) / timestep_given_sampling_frequency)
        datapoints_to_remove_end = int((self.parameters['minutes_to_remove_end'] * 60) / timestep_given_sampling_frequency)

        for item in df:
            new_data = {}
            for channel in item['data'].columns:
                original_length = len(item['data'][channel])
                end_index = max(0, original_length - datapoints_to_remove_end)
                sliced_data = item['data'][channel][datapoints_to_remove_beginning:end_index]
                new_data[channel] = sliced_data.reset_index(drop=True)

            item['data'] = pd.DataFrame(new_data)
            
        return df

    def remove_peaks_and_valleys(self, df):
        print("Removing peaks and valleys...")
        for item in df:
            for channel in item['data'].columns:
                if channel == 'time':
                    continue

                # Calculate the mean and standard deviation of the signal
                mean_signal = np.mean(item['data'][channel])
                std_signal = np.std(item['data'][channel])

                # Set the threshold as 3 standard deviations above and below the mean
                upper_threshold = mean_signal + 3 * std_signal
                lower_threshold = mean_signal - 3 * std_signal

                # Filter elements within the threshold range
                cleaned_signal = item['data'][channel][(item['data'][channel] <= upper_threshold) & (item['data'][channel] >= lower_threshold)]

                # Calculate the 1st (Q1) and 3rd (Q3) quartiles
                Q1 = np.percentile(cleaned_signal, 25)
                Q3 = np.percentile(cleaned_signal, 75)

                # Calculate the IQR
                IQR = Q3 - Q1

                # Define the bounds for filtering
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                # Remove spikes by filtering the cleaned signal
                final_signal = cleaned_signal[(cleaned_signal >= lower_bound) & (cleaned_signal <= upper_bound)]
                
                item['data'][channel] = final_signal
                
            item['data'].dropna(inplace=True)
            item['data'].reset_index(drop=True, inplace=True)
        
        return df
    

    def normalize_data(self, df):
        print("Normalizing data...")
        scaler = StandardScaler()
        for item in df:
            for channel in item['data'].columns:
                if channel == 'time':
                    continue
                # Calculate mean and standard deviation of the channel
                mean_value = item['data'][channel].mean()
                std_dev = item['data'][channel].std()

                # Standardize: (value - mean) / std_dev
                item['data'][channel] = scaler.fit_transform(item['data'][channel].to_numpy().reshape(-1,1))
                
        return df

    def window_data(self, df):
        print("Windowing data...")
        sampling_frequency = 1 / abs(df[0]['data']['time'][1] - df[0]['data']['time'][0]).round(2)
        window_size = self.parameters['window_size']
        datapoints_per_window = int(sampling_frequency * window_size)

        windowed_data = [] 

        for subject in df:
            num_windows = len(subject['data']) // datapoints_per_window
            for window_index in range(num_windows):
                start_index = window_index * datapoints_per_window
                end_index = start_index + datapoints_per_window
                windowed_df = subject['data'].iloc[start_index:end_index]
                
                # Create a new dictionary for the windowed segment
                windowed_data.append({
                    'subject_id': subject['subject_id'],
                    'data': windowed_df,
                    'Y': subject['Y']
                })
                
                
        return windowed_data
    
    def format_data(self, df):
        print("Formatting data...")
        column_names = parameters['channels'][1:] #Förutsatt att time är första kanalen
        empty_df = []
        y_df = []

        for item in df:
            row = []
            
            for channel in column_names:
                temp = item['data'][channel].to_numpy()
                row.append(temp)
            row.append(item['subject_id'])
            row.append(item['Y'])
            empty_df.append(row)
            
        column_names.append('subject_id')   
        column_names.append('Y')
        df_x = pd.DataFrame(empty_df, columns=column_names)
        random_sample_per_category = df_x.groupby('subject_id').apply(lambda x: x.sample(parameters['samples_per_subject'])).reset_index(drop=True)
        df_y = random_sample_per_category['Y']
        df_x = random_sample_per_category.drop(columns=['Y'])
        
        sgkf = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)

        groups = df_x['subject_id']
        # Perform the split
        for train_idx, test_idx in sgkf.split(df_x, df_y, groups=groups):
            X_train, X_test = df_x.iloc[train_idx], df_x.iloc[test_idx]
            y_train, y_test = df_y.iloc[train_idx], df_y.iloc[test_idx]
            break  # Only need the first split
        
        return X_train, X_test, y_train, y_test
    
    
    def process_data(self):
        print("Starting dataloader...")
        print("==================================")
        start_time = time.time()    
        df = self.load_data()
        df_without_outliers = self.remove_outliers(df)
        df_with_selected_subjects = self.select_subjects(df_without_outliers)
        df_with_selected_channels = self.select_channels(df_with_selected_subjects)
        df_trimmed = self.trim_df(df_with_selected_channels)
        df_without_peaks_and_valleys = self.remove_peaks_and_valleys(df_trimmed)
        df_windowed = self.window_data(df_without_peaks_and_valleys)
        df_normalized = self.normalize_data(df_windowed)
        X_train, X_test, y_train, y_test = self.format_data(df_normalized)
        
        end_time= time.time()
        
        print(f"Data processed in: {end_time - start_time} seconds")
        return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    parameters = {
        "sampling_frequency": 100,
        "minutes_to_remove_beginning": 2,
        "minutes_to_remove_end": 2,
        "normalize": True,
        "num_A": 15, # Antal personer med Alzheimers
        "num_F": 0, # Antal personer med Frontotemporal demens
        "num_C": 15, # Antal personer från kontrollgruppen
        "test_size": 0.2,
        "train_size": 0.8,
        "channels": ['time', 'Fp1', 'Fp2', 'Cz', 'Pz'] , # Namn på kanalerna som
        "window_size": 2, # Window size i sekunder
        "random_seed": 42,
        "samples_per_subject": 2
    }
    
    data_loader = CustomDataLoader(parameters)
    X_train, X_test, y_train, y_test = data_loader.process_data()
    
    X_train.to_csv('./X_train.csv', index=False)
    X_test.to_csv('./X_test.csv', index=False)
    y_train.to_csv('./y_train.csv', index=False)
    y_test.to_csv('./y_test.csv', index=False)
import pandas as pd
import numpy as np
import mne_bids
from mne_bids import BIDSPath, read_raw_bids
import matplotlib.pyplot as plt
import os
import mne
import time

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
        print(f"DF before removal {len(df)}")
        outliers_ids = ['sub-026', 'sub-044', 'sub-063'] # Remove outliers given information from t-SNE plot 
        df_without_outliers = [x for x in df if x['subject_id'] not in outliers_ids]
        print(f"DF after removal {len(df_without_outliers)}")
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
                
                mean_value = item['data'][channel].mean()
                std_dev = item['data'][channel].std()

                clip_lower = mean_value - (2 * std_dev) 
                clip_upper = mean_value + (2 * std_dev)
                item['data'][channel] = item['data'][channel].clip(lower=clip_lower, upper=clip_upper)
                
        return df

    def normalize_data(self, df):
        print("Normalizing data...")
        for item in df:
            for channel in item['data'].columns:
                if channel == 'time':
                    continue
                # Calculate mean and standard deviation of the channel
                mean_value = item['data'][channel].mean()
                std_dev = item['data'][channel].std()

                # Standardize: (value - mean) / std_dev
                item['data'][channel] = (item['data'][channel] - mean_value) / std_dev
                
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
                new_subject_id = f"{subject['subject_id']}-{window_index + 1}"
                
                # Create a new dictionary for the windowed segment
                windowed_data.append({
                    'subject_id': new_subject_id,
                    'data': windowed_df,
                    'Y': subject['Y']
                })
                
        return windowed_data

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
        df_normalized = self.normalize_data(df_without_peaks_and_valleys)
        df_windowed = self.window_data(df_normalized)
        
        end_time= time.time()
        
        print(f"Data processed in: {end_time - start_time} seconds")
        return df_windowed

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
        "window_size": 10, # Window size i sekunder
        "random_seed": 42
    }
    data_loader = CustomDataLoader(parameters)
    df = data_loader.process_data()
    print("Subject 1, first window")
    print(df[0]['subject_id'])
    print(df[0]['data'].head())
    print(df[0]['data'].tail())
        
    print("Subject 1, second window")
    print(df[1]['subject_id'])
    print(df[0]['data'].head())
    print(df[0]['data'].tail())

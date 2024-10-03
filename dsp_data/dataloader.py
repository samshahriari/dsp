
import pandas as pd
import numpy as np
import mne_bids
from mne_bids import BIDSPath, read_raw_bids
import matplotlib.pyplot as plt
import os
import mne
import time


"""
Idé: 

Format för input till modellen 
Ex np.array(89, 4, 10000) 
Två npz-filer, en för träningsdata och en för testdata, många personer och få windows

1 - Ladda hela datasetet för alla subjekt
2 - Välj ut vilka datapunkter vi vill ha med (Hur många från varje kontrollgrupp)
3 - Resample till önskad frekvens
4 - Välj ut vilka kanaler vi vill ha med
5 - Ta bort första x sista y minuter (Gör för alla personer, alla kanaler)
6 - Ta bort alla avvikelser som är större än
7 - Normalisera datan över kanaler (Normalisera till 0 mean och 1 std) (Använd bibliotek) Exempel medelvärde: -3.8695041380163586e-16 
8 - Dela upp i fönster med en bestämd längd

Slutprodukt: Spara som dataframe 
# training_data_f = person X kanaler X datapunker/tid(10 s)
# {person 1.1 : {k1: xxxxxxxxxx, k2: xxx, k3: xxx}} Y=dement
# {person 1.2 : {k1: xxx, k2: xxx, k3: xxx}} Y = dement
# {person 1.3 : {k1: xxx, k2: xxx, k3: xxx}}
# {person 2.1 : {k1: xxx, k2: xxx, k3: xxx}} Y = frisk
# {person 2.2 : {k1: xxx, k2: xxx, k3: xxx}}
# {person 2.3 : {k1: xxx, k2: xxx, k3: xxx}}



"""

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

def load_data():
    
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
            raw.resample(sfreq=parameters["sampling_frequency"])
            data = raw.to_data_frame()
            df.append({"subject_id": raw.info['subject_info']['his_id'], "data": data, "Y": raw.info['subject_info']['Group']})

    return df  

def remove_outliers(df):
    print("Removing outliers...")
    print(f"DF before removal {len(df)}")
    outliers_ids = ['sub-026', 'sub-044', 'sub-063'] # Remove outliers given information from t-SNE plot 
    df_without_outliers = [x for x in df if x['subject_id'] not in outliers_ids]
    print(f"DF after removal {len(df_without_outliers)}")
    return df_without_outliers

def select_subjects(df):
    np.random.seed(parameters["random_seed"])

    A_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'A'], parameters["num_A"], replace=False)
    F_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'F'], parameters["num_F"], replace=False)
    C_indicies = np.random.choice([i for i, x in enumerate(df) if x['Y'] == 'C'], parameters["num_C"], replace=False)

    print(f"A Indicies: {A_indicies}")
    print(f"F Indicies: {F_indicies}")
    print(f"C Indicies: {C_indicies}")

    df = [df[i] for i in A_indicies] + [df[i] for i in F_indicies] + [df[i] for i in C_indicies]
    np.random.shuffle(df)
    return df
    
def select_channels(df):
    print("Selecting channels...")
    for item in df:
        for channel in item['data'].columns:
            if channel not in parameters['channels']:
                item['data'].drop(channel, axis=1, inplace=True)
                
    return df
                
def trim_df(df):
    print("Trimming data...")
    timestep_given_sampling_frequency = df[0]['data']['time'][1]
    datapoints_to_remove_beginning = int((parameters['minutes_to_remove_beginning'] * 60) / timestep_given_sampling_frequency)
    datapoints_to_remove_end = int((parameters['minutes_to_remove_end'] * 60) / timestep_given_sampling_frequency)

    for item in df:
  
        new_data = {}
        
        for channel in item['data'].columns:
            original_length = len(item['data'][channel])
            end_index = max(0, original_length - datapoints_to_remove_end)
            sliced_data = item['data'][channel][datapoints_to_remove_beginning:end_index]
            new_data[channel] = sliced_data.reset_index(drop=True)

        item['data'] = pd.DataFrame(new_data)
        
    return df

def remove_peaks_and_valleys(df):
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

def normalize_data(df):
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

def window_data(df):
    print("Windowing data...")
    sampling_frequency = 1 / abs(df[0]['data']['time'][1] - df[0]['data']['time'][0]).round(2)
    window_size = parameters['window_size']
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

def main():
    print("Starting dataloader...")
    print("==================================")
    start_time = time.time()    
    df = load_data()
    df_without_outliers = remove_outliers(df)
    df_with_selected_subjects = select_subjects(df_without_outliers)
    df_with_selected_channels = select_channels(df_with_selected_subjects)
    df_trimmed = trim_df(df_with_selected_channels)
    df_without_peaks_and_valleys = remove_peaks_and_valleys(df_trimmed)
    df_normalized = normalize_data(df_without_peaks_and_valleys)
    df_windowed = window_data(df_normalized)
    
    print("Subject 1, first window")
    print(df_windowed[0]['subject_id'])
    print(df_windowed[0]['data'].head())
    print(df_windowed[0]['data'].tail())
    
    print("Subject 1, second window")
    print(df_windowed[1]['subject_id'])
    print(df_windowed[0]['data'].head())
    print(df_windowed[0]['data'].tail())
    
    end_time= time.time()
    
    print(f"Data processed in: {end_time - start_time} seconds")



main()
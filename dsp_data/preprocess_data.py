import numpy as np
from mne_bids import BIDSPath, read_raw_bids
import pandas as pd

bids_root = 'C:\\Users\\samsh\\Documents\\kurser\\dsp\\dsp_data\\eeg-dataset' 
subject = '001'   
task = 'eyesclosed'
datatype = 'eeg'
suffix = 'eeg'
sampling_rate = 100
time_of_series = 10

bids_path = BIDSPath(subject=subject, task=task, datatype=datatype, suffix=suffix, extension='.set', root=bids_root, check=False)
raw = read_raw_bids(bids_path, verbose=True)
raw = raw.resample(sampling_rate)
raw.plot_sensors(show_names=True)

df = raw.to_data_frame()

fp1_array = df['Fp1'].to_numpy()
fp2_array = df['Fp2'].to_numpy()
pz_array = df['Pz'].to_numpy()
time_array = df['time'].to_numpy()

participants_info = pd.read_csv(bids_root +'/participants.tsv', sep='\t')
# participants_info['']

# training_data_f = person X kanaler X datapunker/tid(10 s)
# {person 1.1 : {k1: xxxxxxxxxx, k2: xxx, k3: xxx}} Y=dement
# {person 1.2 : {k1: xxx, k2: xxx, k3: xxx}} Y = dement
# {person 1.3 : {k1: xxx, k2: xxx, k3: xxx}}
# {person 2.1 : {k1: xxx, k2: xxx, k3: xxx}} Y = frisk
# {person 2.2 : {k1: xxx, k2: xxx, k3: xxx}}
# {person 2.3 : {k1: xxx, k2: xxx, k3: xxx}}

# training_data = np.column_stack((fp1_array, fp2_array, pz_array, time_array))

# training_data_t =
training_data_f = [] 
training_data_t = []
training_data_y = [] 
for i in range(0,len(time_array), sampling_rate*time_of_series):
    sublist = fp1_array[i:i+time_of_series*sampling_rate]
    training_data_f.append(sublist)

    sublist = time_array[i:i+time_of_series*sampling_rate]
    training_data_t.append(sublist)
    
    # sublist_t = time_array[i:i+time_of_series*sampling_rate]
    # print(training_data_t[-1][-1], training_data_f[-1][-1])
    training_data_y.append(participants_info.iloc[int(subject)-1].to_dict()) # {'participant_id': 'sub-001', 'Gender': 'F', 'Age': 57, 'Group': 'A', 'MMSE': 16}

# remove last row as it may be shorter than time_of_series
del training_data_f [-1]
del training_data_t [-1]
del training_data_y [-1]
print(training_data_t[-1][-1], training_data_f[-1][-1], training_data_y[-1])




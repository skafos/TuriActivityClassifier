# Activity classifier prototype with Turi Create
# Based on example from https://apple.github.io/turicreate/docs/userguide/activity_classifier/

import turicreate as tc
from s3fs.core import S3FileSystem
from skafossdk import Skafos
import pandas as pd
import sys

tc.config.set_num_gpus(0)

ska = Skafos()

python_version = sys.version_info[0]

ska.log(f"Python Version: {python_version}", labels = ['activity_classifier'])


# Read in input data and convert to SFrame for modeling
# https://apple.github.io/turicreate/docs/userguide/activity_classifier/data-preparation.html

# Load labels into data frame: Note that all data has been put on s3
data_dir = "https://s3.amazonaws.com/skafos.example.data/HaptDataSet/RawData/"
labels = tc.SFrame.read_csv(data_dir + 'labels.txt', delimiter=' ', header=False, verbose=False)
labels = labels.rename({'X1': 'exp_id', 'X2': 'user_id', 'X3': 'activity_id', 'X4': 'start', 'X5': 'end'})
print("Reading in the example data from Skafos Public S3 bucket ...")

# Import accelerometer and gyroscope data for each experiment. 
# Note that we've had to modify the example data prep code since SFrame.read_csv does not work with s3fs

# Get list of files
s3 = S3FileSystem(anon=True)
directory_path = "s3://skafos.example.data/HaptDataSet/RawData/";
acc_files = s3.glob(directory_path + 'acc_*.txt')
gyro_files = s3.glob(directory_path + 'gyro_*.txt')

# Define function to find appropriate labels for time intervals in data. 
# Users do different activities at different times. We need to find time intervals for each activity and label appropriately. 
# We'll use this in the next loop
def find_label_for_containing_interval(intervals, index):
    containing_interval = intervals[:, 0][(intervals[:, 1] <= index) & (index <= intervals[:, 2])]
    if len(containing_interval) == 1:
        return containing_interval[0]

data = tc.SFrame()
files = zip(sorted(acc_files), sorted(gyro_files))
files_read = 0
ska.report("Files Read", y = files_read, y_label = "Count")
print("Reading in more files....")
for acc_file, gyro_file in files:
    exp_id = int(acc_file.split('_')[1][-2:])
    
    acc_full_path = "s3://" + acc_file
    gyro_full_path = "s3://" + gyro_file
    
    # Read files as pandas data frame and then convert to SFrame, since SFrame does not currenly play nicely with s3fs. 
    # Accel data first then gyro
    
    # Load accel data
    acc_pd = pd.read_csv(s3.open(acc_full_path, mode='rb'), sep=' ', header=None, index_col=False)
    sf = tc.SFrame(data=acc_pd)
    sf = sf.rename({'0': 'acc_x', '1': 'acc_y', '2': 'acc_z'})
    sf['exp_id'] = exp_id

    # Load gyro data
    gyro_pd = pd.read_csv(s3.open(gyro_full_path, mode='rb'), sep=' ', header=None, index_col=False)
    gyro_sf = tc.SFrame(data=gyro_pd)
    gyro_sf = gyro_sf.rename({'0': 'gyro_x', '1': 'gyro_y', '2': 'gyro_z'})
    sf = sf.add_columns(gyro_sf)

    # Calc labels
    exp_labels = labels[labels['exp_id'] == exp_id][['activity_id', 'start', 'end']].to_numpy()
    sf = sf.add_row_number()
    sf['activity_id'] = sf['id'].apply(lambda x: find_label_for_containing_interval(exp_labels, x))
    sf = sf.remove_columns(['id'])
    files_read += 1
    ska.report("Files Read", y = files_read, y_label = "Count")
    data = data.append(sf)
    
# Encode labels 

# For this exercise, we only care about labels 1-6. The remaining labels are removed in the code below. 
# Note also that the full set of labels can be found in HaptDataSet/activity_labels.txt

target_map = {
    1.: 'walking',          
    2.: 'climbing_upstairs',
    3.: 'climbing_downstairs',
    4.: 'sitting',
    5.: 'standing',
    6.: 'laying'
}

print("filtering the data")
# Use the same labels used in the experiment
data = data.filter_by(list(target_map.keys()), 'activity_id')
data['activity'] = data['activity_id'].apply(lambda x: target_map[x])
data = data.remove_column('activity_id')



#Train/test split for modeling
print("split the data for modeling")
train, test = tc.activity_classifier.util.random_split_by_session(data, session_id='exp_id', fraction=0.8)

# Create an activity classifier
print("Creating the activity classifier.....")
model = tc.activity_classifier.create(train, session_id='exp_id', target='activity', prediction_window=50)

print("Evaluate the model....")
# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test)
print(metrics['accuracy'])
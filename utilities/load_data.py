import pandas as pd
import turicreate as tc
from s3fs.core import S3FileSystem


def find_label_for_containing_interval(intervals, index):
    # supporting function for calculating labels
    containing_interval = intervals[:, 0][(intervals[:, 1] <= index) & (index <= intervals[:, 2])]
    if len(containing_interval) == 1:
        return containing_interval[0]


class ActivityData:
    '''
        This class is a restructured version of the data preparation code provided by Turi Create here:
         https://apple.github.io/turicreate/docs/userguide/activity_classifier/data-preparation.html

        It takes the HAPT example data and formats it in a way that it can be used by
        the tc.activity_classifier class of functions.

        Usage: 
            activity_data = ActivityData()
            data = activity_data.get_data()

        see activity_classifier.py
    '''
    def __init__(self):
        self.data_dir = "skafos.example.data/HaptDataSet/RawData/";
        self.data_url = "https://s3.amazonaws.com/" + self.data_dir
        self.label_trans = {
                        'X1': 'exp_id',
                        'X2': 'user_id',
                        'X3': 'activity_id',
                        'X4': 'start',
                        'X5': 'end'
                        }
        self.target_map = {
                1.: 'walking',
                2.: 'climbing_upstairs',
                3.: 'climbing_downstairs',
                4.: 'sitting',
                5.: 'standing',
                6.: 'laying'
            }
        self.s3 = S3FileSystem(anon=True)

    def get_labels(self):
        # read in the labels file from S3
        labels = tc.SFrame.read_csv(self.data_url + 'labels.txt', delimiter=' ', header=False, verbose=False)
        labels = labels.rename(self.label_trans) # translate the labels
        return labels

    def find_files(self):
        # look for all acc (accelerator) files
        acc_files = self.s3.glob("s3://" + self.data_dir + "acc_*.txt")
        # look for all gyro (gyroscope) files
        gyro_files = self.s3.glob("s3://" + self.data_dir + "gyro_*.txt")
        files = zip(sorted(acc_files), sorted(gyro_files))
        return files

    def build_df(self, files):
        data = tc.SFrame() # set an empty data frame that we will append to
        for acc_file, gyro_file in files:
            exp_id = int(acc_file.split('_')[1][-2:])
            acc_full_path = "s3://" + acc_file
            gyro_full_path = "s3://" + gyro_file
    
            # Read files as pandas data frame and then convert to SFrame, since SFrame does not currenly play nicely with s3fs. 
            # Accel data first then gyro
    
            # Load accel data
            acc_pd = pd.read_csv(self.s3.open(acc_full_path, mode='rb'), sep=' ', header=None, index_col=False)
            sf = tc.SFrame(data=acc_pd)
            sf = sf.rename({'0': 'acc_x', '1': 'acc_y', '2': 'acc_z'})
            sf['exp_id'] = exp_id
             # Load gyro data
            gyro_pd = pd.read_csv(self.s3.open(gyro_full_path, mode='rb'), sep=' ', header=None, index_col=False)
            gyro_sf = tc.SFrame(data=gyro_pd)
            gyro_sf = gyro_sf.rename({'0': 'gyro_x', '1': 'gyro_y', '2': 'gyro_z'})
            sf = sf.add_columns(gyro_sf)
            labels = self.get_labels()
            # Calc labels
            exp_labels = labels[labels['exp_id'] == exp_id][['activity_id', 'start', 'end']].to_numpy()
            sf = sf.add_row_number()
            sf['activity_id'] = sf['id'].apply(lambda x: find_label_for_containing_interval(exp_labels, x))
            sf = sf.remove_columns(['id'])
            data = data.append(sf)
        return data

    def get_data(self):
        print("Loading data from S3, this may take a minute", flush=True)
        # get the list of all files from the S3 directory
        files = self.find_files()
        # build the data frame by ingesting and reformatting the data in each file
        df = self.build_df(files)
        print("Data loaded from S3, filter down to the required labels.", flush=True)
        # The target_map defined above only specifies activity labels 1-6
        # in the provided data. The remaining labels are removed in the code below.
        # The full set of labels can be found in HaptDataSet/activity_labels.txt
        data = df.filter_by(list(self.target_map.keys()), 'activity_id')
        
        # translate the acitivity id column
        data['activity'] = data['activity_id'].apply(lambda x: self.target_map[x])
        data = data.remove_column('activity_id') # drop activity id
        data = data.to_dataframe()
        data.columns = ['Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z', 'Experiment', 'Gyroscope_X', 'Gyroscope_Y', 'Gyroscope_Z', 'Activity']

        data = data[['Experiment', 'Activity', 'Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z', 'Gyroscope_X', 'Gyroscope_Y', 'Gyroscope_Z']]

        return tc.SFrame(data)
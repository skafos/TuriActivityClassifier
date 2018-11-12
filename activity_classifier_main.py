# Activity classifier prototype with Turi Create
# Based on example from https://apple.github.io/turicreate/docs/userguide/activity_classifier/

import turicreate as tc
#from skafossdk import Skafos
from load_data import ActivityData
import sys

#ska = Skafos()
activity_data = ActivityData()
tc.config.set_num_gpus(0)

python_version = sys.version_info[0]
#ska.log(f"Python Version: {python_version}", labels = ['activity_classifier'])

# get the data from the load_data module
data = activity_data.get_data()

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
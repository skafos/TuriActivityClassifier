# Activity classifier prototype with Turi Create
# Based on example from https://apple.github.io/turicreate/docs/userguide/activity_classifier/
import turicreate as tc
from skafossdk import *
import sys
import pandas as pd
from common.load_data import ActivityData

ska = Skafos() # initialize Skafos


ska.log("Grabbing the data", labels = ['activity_classifier'])
# load data loading class
activity_data = ActivityData()
data = activity_data.get_data()


# don't use GPU for now
tc.config.set_num_gpus(0)

# get the data
ska.log("Grabbing the data from the public S3 bucket", labels = ['activity_classifier'])

#Train/test split for modeling
ska.log("Splitting the data for modeling", labels = ["activity_classifier"])
train, test = tc.activity_classifier.util.random_split_by_session(data, session_id='Experiment', fraction=0.8)

# Create an activity classifier
ska.log("Creating the activity classifier", labels = ["activity_classifier"])
model = tc.activity_classifier.create(train, session_id='Experiment', target='Activity', prediction_window=50)

ska.log("Evaluating the activity classifier model", labels = ['acitivity_classifier'])
# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test)

ska.log(f"Accuracy metrics from the model: {metrics['accuracy']}", labels = ['activity_classifier'])

# save the model
ska.engine.save_model('Activity-Classifier', model, tags = ['latest'])
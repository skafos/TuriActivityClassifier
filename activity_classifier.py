# Activity classifier prototype with Turi Create
# Based on example from https://apple.github.io/turicreate/docs/userguide/activity_classifier/
import turicreate as tc
from skafossdk import *
import sys
import pandas as pd
from common.load_data import ActivityData
import common.save_models as sm


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


# Evaluate the model and save the results into a dictionary
ska.log("Evaluating the activity classifier model", labels = ['acitivity_classifier'])
metrics = model.evaluate(test)


ska.log("Saving the model", labels = ['activity_classifier'])
# export to coreml
coreml_model_name = "activity_classifier.mlmodel"
res = model.export_coreml(coreml_model_name)

# compress the model
compressed_model_name, compressed_model = compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')


# Turi Create Activity Classifier on Skafos

The example included in this repository is an activity classifier running on Skafos. The model was trained on the open source HAPT dataset. 
  
  Walking             |  Running
:-------------------------:|:-------------------------:
![alt text](https://cdn-images-1.medium.com/max/1120/1*vUB5BP_Fs09Add2P5QV16Q.png "Logo Title Text 1")  |  ![alt_text](https://cdn-images-1.medium.com/max/1120/1*ZXXlUT8jOuYJw6mpGCJEJQ.png "Logo Title Text 2")
 
Thanks to [Viktor Malyi's 4-part article Run or Walk](https://towardsdatascience.com/run-or-walk-detecting-user-activity-with-machine-learning-and-core-ml-part-1-9658c0dcdd90) for the images.
  
## What can you find in this repo?
- `activity_classifer.py` - The main executable that trains the activitiy classifier.
- `activity.model` & `activity.mlmodel` - A pre-trained TuriCreate model and CoreML model.
- `activity_classifier.ipynb` - A Jupyter Notebook containing the same code as 'activity_classifier'
- `Activity_Data_Integration_Example.ipynb` - A Jupyter Notebook containing an example of how to get your own data working in the TuriCreate framework.
- `/models` - a directory that contains a saved TuriCreate model (`.model`) and a saved CoreML model (`.mlmodel`)


## What do I do with it?
- If you want to use this model in your app to detect activities such as standing, walking, running, standing up, sitting down and laying down, download the model and incorporate it into your model.
- If you want to train the model yourself, sign up for a Skafos project, follow these steps and watch it train.
- If you want to train the model on different data, take a look below.


## The Data
The data used to tran this model looks like the following:
- There are 6 measurements, 3 axes collected from an accelerometer and 3 axes collected from a Gyroscope.
- The measurements are associated with an 'Experiment' and an 'Activity'.

In general, so long as you can collect the 3 dimensions from each sensor and associate them with an activity and the "experiment" of that activity, you can pre-train the model on any activity you would like (jumping, throwing, falling). "Experiments" are generally around 50 samples of activity measurements tagged with whatever activity was occuring during that time segment. 

|    |   Experiment | Activity   |   Accelerometer_X |   Accelerometer_Y |   Accelerometer_Z |   Gyroscope_X |   Gyroscope_Y |   Gyroscope_Z |
|---:|-------------:|:-----------|------------------:|------------------:|------------------:|--------------:|--------------:|--------------:|
|  0 |            1 | standing   |           1.02083 |         -0.125    |          0.105556 |  -0.00274889  |  -0.00427606  |    0.00274889 |
|  1 |            1 | standing   |           1.025   |         -0.125    |          0.101389 |  -0.000305433 |  -0.00213803  |    0.00610865 |
|  2 |            1 | standing   |           1.02083 |         -0.125    |          0.104167 |   0.0122173   |   0.000916298 |   -0.00733038 |
|  3 |            1 | standing   |           1.01667 |         -0.125    |          0.108333 |   0.011301    |  -0.0018326   |   -0.00641409 |
|  4 |            1 | standing   |           1.01806 |         -0.127778 |          0.108333 |   0.0109956   |  -0.00152716  |   -0.00488692 |

# ...

|        |   Experiment | Activity          |   Accelerometer_X |   Accelerometer_Y |   Accelerometer_Z |   Gyroscope_X |   Gyroscope_Y |   Gyroscope_Z |
|-------:|-------------:|:------------------|------------------:|------------------:|------------------:|--------------:|--------------:|--------------:|
| 748401 |           61 | climbing_upstairs |          0.880556 |         -0.390278 |        -0.156944  |       1.1637  |      1.10628  |    -0.374155  |
| 748402 |           61 | climbing_upstairs |          0.834722 |         -0.358333 |        -0.0986111 |       1.17714 |      1.02381  |    -0.388816  |
| 748403 |           61 | climbing_upstairs |          0.802778 |         -0.329167 |        -0.104167  |       1.21348 |      0.91813  |    -0.332311  |
| 748404 |           61 | climbing_upstairs |          0.770833 |         -0.2875   |        -0.0986111 |       1.32619 |      0.846659 |    -0.202502  |
| 748405 |           61 | climbing_upstairs |          0.718056 |         -0.268056 |        -0.0555556 |       1.45875 |      0.783129 |    -0.0736093 |

- To find out more about how this data was generated, take a look at the following [link](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones).
- To see the data being generated, take a look at this [video](https://www.youtube.com/watch?v=XOEN9W05_4A).
- If your app doesn't already collect motion data, check out [this app](https://itunes.apple.com/us/app/sensor-kinetics/id579040333?mt=8) that allows you to mess around with the gyroscope and accelerometer on your iPhone.

## How do I integrate my own data?
- Turi Create provides some example code on how to aggregate iOS sensor readings and how to make predictions [here](https://apple.github.io/turicreate/docs/userguide/activity_classifier/export_coreml.html)
- In Viktor Malyi's article mentioned above, he uploaded his own running and walking data to Kaggle. 
- To see how we took Viktor's data and formatted it such that TuriCreate could train a model over his data, check out this repo's [Activity_Data_Integration_Example.ipynb](https://github.com/griffinwalkerMM/TuriActivityClassifier/blob/master/Activity_Data_Integration_Example.ipynb) notebook.

## Going beyond the TuriCreate example
Out of the box, Turi Create gives a great,easy implementation of an Activity Classifier. To go beyond this and make your classifier more sophisticated, Turi Create has some [really great documentation](https://apple.github.io/turicreate/docs/userguide/activity_classifier/).

- For example, both Viktor Malyi's data and the HAPT data set in the original example sampled data from a given experiment/session at a rate of 50 Hz. The example used a `prediction_window` of 50. What does this mean?

*" ... if we want to produce a prediction every 5 seconds, and the sensors are sampled at 50Hz - we would set the prediction_window to 250 (5 sec * 50 samples per second)... Since we have created the model with samples taken at 50Hz and set the prediction_window to 50, we will get one prediction per second. "*.

One can play around with the prediction window to see how it changes model output but also it may have to be adjusted depending on the frequency at which you are sampling your activity data. 

### To try this out:
  - Fork this repo
  - Sign up for a Skafos login
  - Adapt the config files
  - `git push skafos`


# Turi Create Activity Classifier on Skafos

The example included in this repository is an activity classifier running on Skafos taken from a [Turi Create example](https://apple.github.io/turicreate/docs/userguide/activity_classifier/). The model was trained on the open source HAPT dataset. To learn more about how this model works checkout [Turi Create's documentation](https://apple.github.io/turicreate/docs/userguide/activity_classifier/how-it-works.html).

  
## What can you find in this repo?
- `activity_classifer.py` - The main executable that trains the activitiy classifier.
- `activity.model` & `activity.mlmodel` - A pre-trained TuriCreate model and CoreML model.
- `activity_classifier.ipynb` - A Jupyter Notebook containing the same code as 'activity_classifier'
- `Activity_Data_Integration_Example.ipynb` - A Jupyter Notebook containing an example of how to get your own data working in the TuriCreate framework.
- `/models` - a directory that contains a saved TuriCreate model (`.model`) and a saved CoreML model (`.mlmodel`)
- `/common` - a directory that contains functions and code called from the main activity classifier script.


## How to use this repo?
1. Use the `.mlmodel` file in your app to classify activities.
2. Use the provided code and example data to train an activity classifier.
3. Train an activity classifier on different data.
  - To see how we took Viktor's data and formatted it such that TuriCreate could train a model over his data, check out this repo's [Activity_Data_Integration_Example.ipynb](https://github.com/griffinwalkerMM/TuriActivityClassifier/blob/master/Activity_Data_Integration_Example.ipynb) notebook.
  - One can play around with the prediction window to see how it changes model output but also it may have to be adjusted depending on the frequency at which you are sampling your activity data. 



## The Data
The data used to train this model is the publicly available [HAPT data set](https://archive.ics.uci.edu/ml/datasets/Smartphone-Based+Recognition+of+Human+Activities+and+Postural+Transitions). When using the activity_classifier.py to train the model, we use a copy of this data set that has been placed on a public S3 bucket.

In order to train this model with Turi Create, the HAPT Data set needed to be wrangled into the format shown below. The code to do this was adapted from [Turi Create's example](https://apple.github.io/turicreate/docs/userguide/activity_classifier/data-preparation.html) and can be found [here](https://github.com/griffinwalkerMM/TuriActivityClassifier/blob/master/common/load_data.py).

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

The general format of this data is that each experiment contains 6 measurements. 3 axes collected from an accelerometer and 3 axes collected from a gyroscope. Each experiment also contains a labeled activity (e.g. walking, running, standing, etc.)

In general, so long as you can collect the 3 dimensions from each sensor and associate them with an activity and the "experiment" of that activity, you can pre-train the model on any activity you would like (jumping, throwing, falling). An example of how to do this is described above.

- To find out more about how this data was generated, take a look at the following [link](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones).
- To see the data being generated, take a look at this [video](https://www.youtube.com/watch?v=XOEN9W05_4A).
- If your app doesn't already collect motion data, check out [this app](https://itunes.apple.com/us/app/sensor-kinetics/id579040333?mt=8) that allows you to mess around with the gyroscope and accelerometer on your iPhone.




### To try this out:
  - Fork this repo
  - Sign up for a Skafos login
  - Adapt the config files
  - `git push skafos`


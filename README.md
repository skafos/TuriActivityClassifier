# Turi Create Activity Classifier on Skafos

The example included in this repository is an activity classifier running on Skafos:

  *"Activity classification is the task of identifying a pre-defined set of physical actions using motion-sensory inputs. Such sensors include accelerometers, gyroscopes, thermostats, and more found in most handheld devices today."*
  
  
  Walking             |  Running
:-------------------------:|:-------------------------:
![alt text](https://cdn-images-1.medium.com/max/1120/1*vUB5BP_Fs09Add2P5QV16Q.png "Logo Title Text 1")  |  ![alt_text](https://cdn-images-1.medium.com/max/1120/1*ZXXlUT8jOuYJw6mpGCJEJQ.png "Logo Title Text 2")
 
Thanks to [Viktor Maly's 4-part article Run or Walk](https://towardsdatascience.com/run-or-walk-detecting-user-activity-with-machine-learning-and-core-ml-part-1-9658c0dcdd90) for the images.
  
## What can you find in this repo?
- `activity_classifer.py` - The main executable that trains the activitiy classifier.
- `activity.model` & `activity.mlmodel` - A pre-trained TuriCreate model and CoreML model.
- `activity_classifier.ipynb` - A Jupyter Notebook containing the same code as 'activity_classifier'

- A support `/common/load_data.py` module that does some initital data cleaning/ prep.


## How do I integrate my own data?
The data used to tran this model looks like the following. You can either use this model as a pre-trained model and make predictions, or you can re-train the model using your own data. For example, if you had different activities that you wanted to classify, like jumping, throwing, and falling.

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

To find out more about how this data was generated, take a look at the following [link](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones). To see the data being generated, take a look at this [video](https://www.youtube.com/watch?v=XOEN9W05_4A).
  
### To try this out:
  - Fork this repo
  - Sign up for a Skafos login
  - Adapt the config files
  - `git push skafos`

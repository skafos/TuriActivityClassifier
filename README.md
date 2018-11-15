# Turi Create Activity Classifier on Skafos

The example included in this repository is an activity classifier running on Skafos:

  *"Activity classification is the task of identifying a pre-defined set of physical actions using motion-sensory inputs. Such sensors include accelerometers, gyroscopes, thermostats, and more found in most handheld devices today."*
  
  See more at **https://apple.github.io/turicreate/docs/userguide/activity_classifier/**.
  
## What can you find in this repo?
- `activity_classifer.py` - The main executable that trains the activitiy classifier.
- `activity.model` & `activity.mlmodel` - A pre-trained TuriCreate model and CoreML model.
- `activity_classifier.ipynb` - A Jupyter Notebook containing the same code as 'activity_classifier'

- A support `/common/load_data.py` module that does some initital data cleaning/ prep.

  
To try this out:
  - Fork this repo
  - Sign up for a Skafos login
  - Adapt the config files
  - `git push skafos`

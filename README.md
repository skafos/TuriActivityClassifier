## Turi Create Activity Classifier on Skafos

The example included in this repository is an activity classifier running on Skafos:

  *"Activity classification is the task of identifying a pre-defined set of physical actions using motion-sensory inputs. Such sensors include accelerometers, gyroscopes, thermostats, and more found in most handheld devices today."*
  *See more at **https://apple.github.io/turicreate/docs/userguide/activity_classifier/** *
  
This repo's main executable is `activity_classifier.py`. This script:
  - Loads data from a public S3 bucket (see `/common/load_data.py`)
  - Splits the data into training and testing
  - Builds the activity classifier using Turi Create's `tc.activity_classifier` function
  - Evaluates the model
  
To try this out:
  - Fork this repo
  - Sign up for a Skafos login
  - Adapt the config files
  - `git push skafos`

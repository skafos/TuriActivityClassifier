# Advanced Usage
The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building activity classification models.

## Tips And "Gotchas"

-  **Training Data**: The training data used for the sentiment classifier consists of raw text from user reviews on Yelp, paired with a sentiment score (1-5). Don't expect the model to predict the topic of text out of the box unless you change the underlying training data.
    -  **Key Point:** When you train a model, the nature of the training data directly influences the model's ability to make 
- **Wrangling Sensor Data w/ Turi Create**: 


## Resources

-  `text_in_turicreate.ipynb`: Gives some tips on adapting your text classifier to a **NEW** set of data, detailing proper formatting and several helper functions.
-  `spam_classifier.ipynb`: Ready to try something other than sentiment classification? Try out spam classification and wrangle a new external data source. By the end, you will have trained a different text classifier and evaluated the model's performance on a holdout test set.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://skafosai.slack.com)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/text_classifier/) on text classification basics.

# How to run

First, install the requirements by doing `pip install -r requirements.txt` in your console (preferably in a virtual environment)

For this project, you will need
- Flask
- tweepy
- nltk
- scikit-learn
- pandas
- numpy
- pickle

Also, to use tweepy, you need to register for a Twitter developer account. The process for this usually takes a while, but they guide you through the process well.

Once this is done, replace the placeholders in `analyze.py` with your codes.

Once your environment is setup and your codes inputted, you have two options:
1. You can edit `fullModelTraining.py` with your own model, hyperparameters, and/or section of the data (I used 100k tweets, but you might want more or less)
2. Or, you could just run `analyze.py` with the existing model (acc ~ 74%)

For analyze.py, when you enter a topic into the field and hit enter, the twitter api will look for the last 10 tweets containing that keyword. Then, it will call them, vectorize and preprocess them like it did to the training data, and run the model you chose on the matrices.

The predictions are displayed to the terminal.

They are also displayed in a table, where they are displayed (cut off), along with their predicted sentiment, positive or negative.

[Project Statement](docs/projectStatement.md) : A web page that will analyze a series of tweets filtered by a topic using the twitter api and use python NLTK to analyze if a tweet is positive or negative.

# How to run

__The data is from [here](https://www.kaggle.com/kazanova/sentiment140)__. Download it and save it as `data.csv` inside the data folder.

This project assumes you have *Python* pre-installed and *pip* setup.

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

Once this is done, replace the placeholders in lines *13-16* in `analyze.py` with your account-specific codes which can be accessed once you create a new app. For a helpful tutorial, refer to [this](https://www.alexkras.com/how-to-get-user-feed-with-twitter-api-and-python/).

Once your environment is setup and your codes inputted, you have two options:
1. You can edit `fullModelTraining.py` with your own model, hyperparameters, and/or section of the data (I used 100k tweets, but you might want more or less)
2. Or, you could just run `analyze.py` with the existing model (acc ~ 74%)

For analyze.py, when you enter a topic into the field and hit enter, the twitter api will look for the last 10 tweets containing that keyword. Then, it will call them, vectorize and preprocess them like it did to the training data, and run the model you chose on the matrices.

The predictions are displayed to the terminal.

They are also displayed in a table, where they are shown (cut off), along with their predicted sentiment, positive or negative.


__Go to the [log](docs/log.md) for a day by day log__

File / Folder explanation
1. Python Files
    * `analyze.py` is the actual Flask app to run
    * `fullModelTraining.py` is the python file to:
        * Read the dataset
        * Preprocess the data
        * Vectorizes the data and saves the TfidfVectorizer
        * Generate the opimum model (default is a BernoulliNB, but can be changed) and save it
        * Run evaluation to terminal to view accuracy and f1-score
2. Templates
    * This contains the templates (html files) used for this program
        * `mainPage.html` is the main page with the form for user input
        * `view.html` is the page which displays the last 10 tweets (topic user chooses), along with their predicted sentiment, in a table form.
3. Static
    * The `style.css` file contains the styling for the webpage
4. Outputs
    * `finalmodel.pkl` contains the final model saved as a pkl file for later use
    * `tfidf.pickle` contains the final TfidfVectorizer for use in vectorizing real time tweets
5. Docs
    * `log.md` contains a day by day log of progress. Does not include bugs and issues, but is helpful for tracking progress
    * `projectStatement.md` contains a project statement for this particular project
6. Data
    * This folder contains the kaggle data of all the tweets. This is used for training purposes, and should be downloaded from the link in the top of the readme and saved as `data.csv` for use in training the model. __Note : Not necessary if not retraining models__.

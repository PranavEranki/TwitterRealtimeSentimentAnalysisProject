from flask import *
import tweepy
import pandas as pd
import numpy as np

import json

from sklearn.externals import joblib
import pickle

from fullModelTraining import cleanTweets

ACCESS_TOKEN = 'Enter_Here'
ACCESS_SECRET = 'Enter_Here'
CONSUMER_KEY = 'Enter_Here'
CONSUMER_SECRET = 'Enter_Here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth)

model = joblib.load("outputs/finalmodel.pkl")
tf = pickle.load(open("outputs/tfidf.pickle", "rb"))

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/tables', methods = ['POST'])
def getTopic():
    topic = request.form['topic']

    tweets = np.asarray(getCleanedResults(topic))
    results = np.asarray(doPredictions(tweets))

    df = pd.DataFrame({"tweets":tweets, "predictions":results})

    for i in range(10):
        print("Tweet : " + tweets[i] + ", pred : " + str(results[i]))

    return render_template('view.html',tables=[df.to_html(classes='data')])

def getCleanedResults(topic):
    results = api.search(q = topic, lang = "en")
    tweets = []
    for i in range(10):
        tweets.append(cleanTweets((results[i].text)))

    return tweets

def doPredictions(tweets):
    tweets = tf.transform(tweets)
    pred2 = model.predict(tweets)

    pred = []
    for p in pred2:
        if (p == 0):
            pred.append("Negative")
        elif (p == 1):
            pred.append("Positive")

    return pred

if __name__ == "__main__":
    app.run()

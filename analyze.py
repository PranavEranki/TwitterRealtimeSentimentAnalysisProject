from flask import *
import tweepy
import json

from fullModelTraining import cleanTweets

ACCESS_TOKEN = '1112133104204836864-JK8hpTMvxOLePQvIhYuxV3oSf4rBh6'
ACCESS_SECRET = 'Pyps7jrDdOapJYVEVHcAk4J7qJwnTapDStlotgCEyaPg1'
CONSUMER_KEY = 'XVkipNLEu8WwcdNoBdGiD9wdE'
CONSUMER_SECRET = 'qOxlkDWfDAV8ZCaPzDyCn4Khgcn4kI1qaVf5yKXTYlUK0MQyda'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth)

model = joblib.load("finalmodel.pkl")
tf = pickle.load(open("tfidf.pickle", "rb"))

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/analyze', methods = ['POST'])
def getTopic():
    topic = request.form['topic']
    # print("Your selected topic is '" + topic + "'")
    # Getting twitter results for that topic
    tweets = getCleanedResults(topic)
    doPredictions(tweets)

    for (i in range(10)):
        print("Tweet : " + getCleanedResults[i] + ", pred : " + str(doPredictions[i]))

    return redirect('/')

def getCleanedResults(topic):
    results = api.search(q = topic, lang = "en")
    tweets = []
    for i in range(10):
        tweets.append(cleanTweets((results[i].text)))

    return tweets

def doPredictions(tweets):
    for tweet in tweets:
        tweet = tf.transform(tweet)

    results = []
    for tweet in tweets:
        results.append(model.predict(tweet))

    return results

if __name__ == "__main__":
    app.run()

from flask import *
import tweepy
import json

ACCESS_TOKEN = 'YOUR ACCESS TOKEN"'
ACCESS_SECRET = 'YOUR ACCESS TOKEN SECRET'
CONSUMER_KEY = 'YOUR API KEY'
CONSUMER_SECRET = 'ENTER YOUR API SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/analyze', methods = ['POST'])
def getTopic():
    topic = request.form['topic']
    print("Your selected topic is '" + topic + "'")

    return redirect('/')

if __name__ == "__main__":
    app.run()

import string
import re

import pandas as pd

from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split

# we want the most data available, so we take all the tweets (20k)
df = pd.read_csv("data/data.csv", encoding = "ISO-8859-1", names = ["target", "ids", "date", "flag", "user", "text"])

# Changing the y values to more human-friendly ones
decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}
def decode_sentiment(label):
    return decode_map[int(label)]
df.target = df.target.apply(lambda x : decode_sentiment(x))
# Getting the stopwords
stopwords_english = stopwords.words('english')
# We want a tweet tokenizer that will split the tweet into a list of words
tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
# Porter stemmer for determining root of word
stemmer = PorterStemmer()

# Now, we need to 'clean' the tweet
def cleanTweets(tweet):
    """
    1. Remove 'RT'
    2. Remove links
    3. Remove punctuation, turn to lowercase
    4. Remove words from nltk's stopwords corpus
    5. Use PorterStemmer to turn each word into its stem
    """
    # Leave only letters
    tweet = re.sub('[^a-zA-Z]', ' ', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # Lower case
    tweet = tweet.lower()

    # Tokenize, remove stopwords
    tweet_tokens = tweet_tokenizer.tokenize(tweet)
    cleaned_tweets = [stemmer.stem(word) for word in tweet_tokens if not word in set(stopwords_english)]

    return cleaned_tweets

# Now, we need to make a bag of words model

cv = CountVectorizer(max_features = 1500) # Remmoves redundant words

def bagOfWords(tweet):
    cleaned = cleanTweets(tweet)
    X = cv.fit_transform(cleaned).toarray()
    return X

for tweet in df.text:
    tweet = bagOfWords(tweet)

print(df.head)

X_train, X_test, y_train, y_test = train_test_split(df.text, df.target, test_size = 0.25, random_state = 0)

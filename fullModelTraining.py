import string
import re
import warnings
warnings.simplefilter("ignore")

import pandas as pd
import numpy as np

from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


def import_tweets(filename, frac, header = None):
	#import data from csv file via pandas library.
    # Only take a certain fraction of the data. We do not need 1.6 million tweets
	tweet_dataset = pd.read_csv(filename, encoding = "ISO-8859-1").sample(frac = frac)
	#the column names are based on sentiment140 dataset provided on kaggle
	tweet_dataset.columns = ['sentiment','id','date','flag','user','text']
	#delete 3 columns: flags,id,user, as they are not required for analysis
	for i in ['flag','id','user','date']: del tweet_dataset[i] # or tweet_dataset = tweet_dataset.drop(["id","user","date","user"], axis = 1)
	#in sentiment140 dataset, positive = 4, negative = 0; So we change positive to 1
	tweet_dataset.sentiment = tweet_dataset.sentiment.replace(4,1)
	return tweet_dataset

# Now, we need to 'clean' the tweet
def cleanTweets(tweet):
    tweet.lower()
    #convert all urls to sting "URL"
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))' , ' ', tweet)
    #convert all @username to "AT_USER"
    tweet = re.sub('@[^\s]+',' ', tweet)
    #correct all multiple white spaces to a single white space
    tweet = re.sub('[\s]+', ' ', tweet)
    #convert "#topic" to just "topic"
    tweet = re.sub(r'#([^\s]+)', ' ', tweet)
    return tweet

def useVectorizer(data, max):
    tfv=TfidfVectorizer(min_df=0, max_features= max, strip_accents='unicode',lowercase =True,
                            analyzer='word', token_pattern=r'\w{3,}', ngram_range=(1,1),
                            use_idf=True,smooth_idf=True, sublinear_tf=True, stop_words = "english") # we need to give proper stopwords list for better performance
    features=tfv.fit_transform(data)
    print ("dataset transformed")
    print ("dataset shape ", features.shape)
    print()
    return features.toarray()

def train_classifier(x_train, y_train, multiple = False, x_test, y_test):
    if (multiple == True):
        models = [GaussianNB(), MultinomialNB(), SVC(), BernoulliNB()]
        for model in models:
            print("Training : " + str(type(model)))
            model.fit(x_train, y_train)
        print()
        return models
    else:
        # Insert optimum model here with optimum parameters
        model = BernoulliNB()
        params = {
        'alpha':(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),
        'fit_prior':(True, False)
        }
        clf = GridSearchCV(model, params, cv = 5, n_jobs=-1)
        clf.fit(x_train, y_train)

        return clf.best_estimator

def testClassifier(cls, x, y):
    if isinstance(cls, (list,)):
        for model in cls:
            print("For model : " + str(type(model)))
            pred = model.predict(x)
            printReports(y, pred)

    else:
        pred = cls.predict(x)
        printReports(y, pred)

def printReports(y, pred):
    rep = classification_report(y, pred)
    cm = confusion_matrix(y, pred)
    accuracy = accuracy_score(y, pred)
    print("F1 score : " + str(rep))
    print("Confusion matrix : " + str(cm))
    print("Accuracy score : " + str(accuracy))
    print()

def full():
    tweet_dataset = import_tweets("data/data.csv", 0.006)
    tweet_dataset['text'] = tweet_dataset['text'].apply(cleanTweets)
    data = np.array(tweet_dataset.text)
    label = np.array(tweet_dataset.sentiment)
    features = useVectorizer(data, 1500)
    x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.25, random_state=0)
    all_models = train_classifier(x_train, y_train, multiple = False, x_test, y_test)
    testClassifier(all_models, x_test, y_test)

if __name__ == "__main__":
    full()

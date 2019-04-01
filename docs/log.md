# Log for tracking progress

## 3/29/2019
- Reviewed some Flask
- Created a webpage that will take a take in a topic and print it to the console for testing purposes

# 3/30/19
- Read up on how to use Twitter API
- Registered for twitter developer account
  - This required me to fill out a form and wait for approval
- Got the data from a kaggle dataset [here](https://www.kaggle.com/kazanova/sentiment140)
- Python code
  - Wrote a cleaning tweet method using regex, porterstemmer, and tokenizer
  - Created a bag of words using tfidf vectorizer
  - Read the data, processed it, and split it
  - Tested different vectorizers and different methods
  - Fixed some bugs in program

# 3/31/19
- Removed some of the preprocessing that was causing errors
- Added some different preprocessing
- Organized code into reusable functions, added folder structure
- Finalized code for single model
  - Added functionality to test various models to determine optimum model
  - Optimum model is BernoulliNB, but MultinomialNB is also viable
  - Ran gridsearchCV on MultinomialNB and Bernoulli using random subsets of the data
  - The average accuracy is about 74%, which is not good but its the best I was able to achieve with sklearn. NNs would be better but also more computationally intensive.
- Trained the single model on 6% of the data, about 100k tweets.
- Wrote code for saving the model and TfidfVectorizer for use by Flask app
- Integrated tweet API
  - Getting last 10 tweets
  - Running vectorizer and cleaning the tweets
  - Predicting using the model, printing out the predictions
- Added full website support. Finished app, polished, put info in readme.

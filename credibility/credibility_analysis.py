import pickle
from ML.vectorisation import vectorisation

with open('ML\\fake_news_AI', 'rb') as pipeline:
    model = pickle.load(pipeline)

def ml_analysis(tweet_txt):
    '''
    Use the ML trained model to estimate the credibility of a tweet.
    Returns a real between 0 and 1, 1 corresponding to most likely fake news.
    '''
    return model.predict_proba(vectorisation(tweet_txt))[0,0]

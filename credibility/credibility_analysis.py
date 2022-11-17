""" Compute the credibility of a tweet, thanks to a ML-trained model. """

import pickle

from ML.vectorisation import vectorisation

with open('ML\\fake_news_AI', 'rb') as pipeline:
    model = pickle.load(pipeline)


def ml_analysis(tweet):
    """ Compute the credibility of the tweet, thanks to a ML-trained model.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    float
        The estimated credibility, between 0 and 1.
        The higher the number is, the most likely the tweet is fake news.
    """
    return model.predict_proba(vectorisation(tweet['tweet_textual_content']))[0, 0]

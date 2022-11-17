""" Sentiment analysis estimation """

from textblob import TextBlob


def sentiment_analysis(tweet):
    """ Estimate the polarity and the subjectivity of a tweet.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    (float, float)
        The first element if the estimated polarity, from -1 (very negative)
        to 1 (very positive). The second element if the estimated subjectivity,
        from 0 (very objective) to 1 (very subjective).
    """

    tweet_blob = TextBlob(tweet['tweet_textual_content']).words
    if 'RT' in tweet_blob:
        tweet_blob = tweet_blob[1:]
    tweet_txt = tweet_blob[1]
    for k in range(2, len(tweet_blob)):
        tweet_txt += ' ' + tweet_blob[k]
    return TextBlob(tweet_txt).sentiment.polarity, TextBlob(tweet_txt).sentiment.subjectivity

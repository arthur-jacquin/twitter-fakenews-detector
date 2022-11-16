from textblob import TextBlob


def sentiment_analysis(tweet):
    '''
    cette fonction donne un score entre 0 et 1 pour un tweet donné
    elle prend en argument une row du dataframe des tweets extraits
    return: tuple (polarity, subjectivity)
    '''
    tweet_blob = TextBlob(tweet['tweet_textual_content']).words
    if 'RT' in tweet_blob:
        tweet_blob = tweet_blob[1:]
    tweet_txt = tweet_blob[1]
    for k in range(2, len(tweet_blob)):
        tweet_txt += ' '+tweet_blob[k]
    # return tweet_txt
    return TextBlob(tweet_txt).sentiment.polarity, TextBlob(tweet_txt).sentiment.subjectivity

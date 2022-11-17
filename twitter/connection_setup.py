""" Module to connect to the Twitter's API

CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_SECRET credentials must be defined in twitter/credentials.py.
"""

import tweepy

from twitter.credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET


def twitter_setup():
    """ Setup the connection to the Twitter's API

    Parameters
    ----------

    Returns
    -------
    Authentified Twitter's API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

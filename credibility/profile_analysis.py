""" Compute informations about a tweet author. """

from time import time
import datetime


def account_age(tweet):
    """ Compute the age of the author account.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    float
        Account age (in seconds) of the tweet author.
    """
    return time() - tweet['user_creation_date'].timestamp()


def number_of_followers(tweet):
    """ Get the number of followers of the tweet author.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    int
        Number of followers of the tweet author.
    """
    return tweet['user_nb_followers']


def number_of_following(tweet):
    """ Get the number of following of the tweet author.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    int
        Number of following of the tweet author.
    """
    return tweet['user_nb_followings']


def ratio_of_statuses_account_age(tweet):
    """ Compute the ratio of statuses to the account age for the tweet author.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    float
        Ratio of statuses to the account age for the tweet author
    """
    return tweet['user_nb_status']/account_age(tweet)

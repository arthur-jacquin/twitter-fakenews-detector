from time import time
import datetime


def account_age(tweet):
    '''
    Get the account age (in seconds) of the tweet author.
    '''
    return time() - tweet['user_creation_date'].timestamp()


def number_of_followers(tweet):
    '''
    Get the number of followers of the tweet author.
    '''
    return tweet['user_nb_followers']


def number_of_following(tweet):
    '''
    Get the number of following of the tweet author.
    '''
    return tweet['user_nb_followings']


def ratio_of_statuses_account_age(tweet):
    '''
    Compute the ratio of statuses by the account age for the tweet author.
    '''
    return tweet['user_nb_status']/account_age(tweet)

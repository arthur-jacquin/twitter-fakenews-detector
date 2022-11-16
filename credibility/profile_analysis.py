from time import time, mktime, strptime

def account_age(tweet):
    '''
    Get the account age of the tweet author.
    '''
    return time() - mktime(strptime(tweet['user_creation_date'], '%a %b %d %H:%M:%S +0000 %Y'))


def number_of_followers(tweet):
    '''
    Get the number of followers of the tweet author.
    '''
    return tweet['user_nb_of_followers']


def number_of_following(tweet):
    '''
    Get the number of following of the tweet author.
    '''
    return tweet['user_nb_of_followers']


def ratio_of_statuses_account_age(tweets):
    '''
    Compute the ratio of statuses by the account age.
    '''
    pass

def account_age(tweet):
    '''
    Get the account age of the tweet author.
    '''
    pass


def number_of_followers(tweet):
    '''
    Get the number of followers of the tweet author.
    '''
    pass


def number_of_following(tweet):
    '''
    Get the number of following of the tweet author.
    '''
    pass


def ratio_age_retweets(tweet):
    '''
    Compute the ratio of retweets of the tweet dataframe.
    '''
    user_id = tweet['user_id']
    age = account_age(tweet)
    nb_tweets = tweet['user_nb_status']
    return age/nb_tweets

from twitter.connection_setup import twitter_setup

import tweepy
import pandas as pd

def collect_tweets(queries, tweet_number):
    '''
    Cette fonction prend en entrée un string de mots clés et un nombre de tweets à analyser
    return: les infos que l'on souhaite pour chaque tweet sous forme de listes
    '''
    # Data to collect
    tweet_textual_content = []
    user_id = []
    tweet_id = []
    user_creation_date = []
    tweet_nb_rt = []
    user_nb_followers = []
    user_nb_followings = []
    user_nb_status = []

    # Connection setup
    api = twitter_setup()

    # Parsing of queries
    queries_list = queries.split('\n')

    for query in queries_list:
        # Query
        res = api.search_tweets(
            query, lang='en', result='popular', count=tweet_number)

        # Collect
        for tweet in res:
            tweet_textual_content.append(tweet.text)
            user_id.append(tweet.user.id)
            tweet_id.append(tweet.id)
            user_creation_date.append(tweet.user.created_at)
            tweet_nb_rt.append(tweet.retweet_count)
            user_nb_followers.append(tweet.user.followers_count)
            user_nb_followings.append(tweet.user.friends_count)
            user_nb_status.append(tweet.user.statuses_count)

    return {
        'tweet_textual_content': tweet_textual_content,
        'user_id': user_id,
        'tweet_id': tweet_id,
        'user_creation_date': user_creation_date,
        'tweet_nb_rt': tweet_nb_rt,
        'user_nb_followers': user_nb_followers,
        'user_nb_followings': user_nb_followings,
        'user_nb_status': user_nb_status,
    }

def transform_to_dataframe(dict_res):
    return pd.DataFrame(dict_res)


def get_rt_author_ids(tweet_id, number):
    '''
    Get the author IDs of the retweets of tweet_id.
    '''
    res = []

    # Connection setup
    api = twitter_setup()

    # Query
    res = api.retweets(tweet_id, number)

    for tweet in res:
        res.append(tweet.user.id)

    return res



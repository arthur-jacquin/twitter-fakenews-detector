from twitter.connection_setup import twitter_setup

import tweepy
import pandas as pd


def transform_to_dataframe(dict_res):
    return pd.DataFrame(dict_res)


def collect_tweets(queries, tweet_number):
    '''
    Cette fonction prend en entrée un string de mots clés et un nombre de tweets à analyser
    return: les infos que l'on souhaite pour chaque tweet sous forme de listes
    '''
    # Data to collect
    tweet_textual_content = []
    user_id = []
    user_name = []
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

    if queries_list == []:
        raise ZeroDivisionError

    for query in queries_list:
        # Query
        res = api.search_tweets(
            query, lang='en', result='popular', count=int(tweet_number/len(queries_list)))

        # Collect
        for tweet in res:
            tweet_textual_content.append(tweet.text)
            user_id.append(tweet.user.id)
            user_name.append(tweet.author.screen_name)
            tweet_id.append(tweet.id)
            user_creation_date.append(tweet.user.created_at)
            tweet_nb_rt.append(tweet.retweet_count)
            user_nb_followers.append(tweet.user.followers_count)
            user_nb_followings.append(tweet.user.friends_count)
            user_nb_status.append(tweet.user.statuses_count)

    return {
        'tweet_textual_content': tweet_textual_content,
        'user_id': user_id,
        'user_name': user_name,
        'tweet_id': tweet_id,
        'user_creation_date': user_creation_date,
        'tweet_nb_rt': tweet_nb_rt,
        'user_nb_followers': user_nb_followers,
        'user_nb_followings': user_nb_followings,
        'user_nb_status': user_nb_status,
    }


def get_rt_author_info(tweet_id, number):
    '''
    Get info on the author of the retweets of tweet_id.
    '''
    # Data to collect
    user_creation_date = []
    user_nb_followers = []
    user_nb_followings = []
    user_nb_status = []

    # Connection setup
    api = twitter_setup()

    # Query
    res = api.get_retweets(tweet_id, count=number)

    # Collect
    for tweet in res:
        user_creation_date.append(tweet.user.created_at)
        user_nb_followers.append(tweet.user.followers_count)
        user_nb_followings.append(tweet.user.friends_count)
        user_nb_status.append(tweet.user.statuses_count)

    return {
        'user_creation_date': user_creation_date,
        'user_nb_followers': user_nb_followers,
        'user_nb_followings': user_nb_followings,
        'user_nb_status': user_nb_status,
    }


def get_tweet_info(tweet_id):
    '''
    Get info on the tweet of id tweet_id.
    '''
    # Connection setup
    api = twitter_setup()

    # Query
    tweet = api.get_status(tweet_id)

    return {
        'tweet_textual_content': tweet.text,
        'user_id': tweet.author.id,
        'user_name': tweet.author.screen_name,
        'tweet_id': tweet.id,
        'user_creation_date': tweet.user.created_at,
        'tweet_nb_rt': tweet.retweet_count,
        'user_nb_followers': tweet.user.followers_count,
        'user_nb_followings': tweet.user.friends_count,
        'user_nb_status': tweet.user.statuses_count,
    }

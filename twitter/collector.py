from twitter.connection_setup import twitter_setup

import tweepy
import pandas as pd


def collect_tweets(queries, tweet_number):
    """
    Cette fonction prend en entrée un string de mots clés et un nombre de tweets à analyser
    return: les infos que l'on souhaite pour chaque tweet sous forme de listes
    """
    # Data to collect
    tweet_textual_content = []
    user_id = []
    tweet_id = []
    user_account_age = []
    tweet_nb_rt = []
    user_nb_followers = []
    user_nb_followings = []

    # Connection setup
    api = twitter_setup()

    # Parsing of queries
    queries_list = queries.split('\n')

    for query in queries_list:
        # Query
        res = api.search_tweets(query, lang='en', count=tweet_number)

        # Collect
        for tweet in res:
            tweet_textual_content.append(tweet.text)
            user_id.append(tweet.user.id)
            tweet_id.append(tweet.id)
            user_account_age.append(tweet.user.created_at)
            tweet_nb_rt.append(tweet.retweet_count)
            user_nb_followers.append(tweet.user.followers_count)
            user_nb_followings.append(tweet.user.friends_count)

    return tweet_textual_content, user_id, tweet_id, user_account_age, tweet_nb_rt, user_nb_followers, user_nb_followings


def transform_to_dataframe(tab):
    return pd.DataFrame({
        'tweet_textual_content': tab[0],
        'user_id': tab[1],
        'tweet_id': tab[2],
        'user_account_age': tab[3],
        'tweet_nb_rt': tab[4],
        'user_nb_followers': tab[5],
        'user_nb_followings': tab[6]})

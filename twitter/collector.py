from twitter.connection_setup import twitter_setup

import tweepy
import pandas as pd


def collect_tweets(queries, tweet_number):
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
        res = api.search_tweets(query, lang='en', count=count)

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


def transform_to_dataframe(tweet_textual_content, user_id, tweet_id, user_account_age, tweet_nb_rt, user_nb_followers, user_nb_followings):
    return pd.DataFrame({
        'tweet_textual_content': tweet_textual_content,
        'RTs': user_id,
        'Source': tweet_id,
        'author': user_account_age,
        'author': tweet_nb_rt,
        'author': user_nb_followers,
        'author': user_nb_followings})

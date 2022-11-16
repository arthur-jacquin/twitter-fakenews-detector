from twitter.connection_setup import twitter_setup

import tweepy
import pandas as pd


def collect_tweets(queries, tweet_number):
    # Data to collect
    content_list = []
    rt_list = []
    source_list = []
    author_list = []

    # Connection setup
    api = twitter_setup()

    # Parsing of queries
    queries_list = queries.split('\n')

    for query in queries_list:
        # Query
        res = api.search_tweets(query, lang='en', count=count)

        # Collect
        for tweet in res:
            content_list.append(tweet.text)
            rt_list.append(tweet.retweet_count)
            source_list.append(tweet.source)
            author_list.append(tweet.author.screen_name)

    return pd.DataFrame({
        'tweet_textual_content': content_list,
        'RTs': rt_list,
        'Source': source_list,
        'author': author_list,
    })

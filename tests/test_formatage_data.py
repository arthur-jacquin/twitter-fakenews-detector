from twitter.collector import collect_tweets
from twitter.collector import transform_to_datframe

from pytest import *


def test_collect():
    tweet = collect_tweets('trump', 3)
    data = transform_to_dataframe(tweet)
    assert 'tweet_textual_content' in data.columns
    assert 'user_id' in data.columns
    assert 'tweet_id' in data.columns
    assert 'user_account_age' in data.columns
    assert 'tweet_nb_rt' in data.columns
    assert 'user_nb_followers' in data.columns
    assert 'user_nb_following' in data.columns

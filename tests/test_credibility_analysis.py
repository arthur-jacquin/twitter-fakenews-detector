from pytest import *
from credibility.credibility_analysis import ml_analysis
from twitter.collector import collect_tweets, transform_to_dataframe

for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_ml_analysis():
    pred = ml_analysis(tweet)
    assert 0 <= pred
    assert pred <= 1

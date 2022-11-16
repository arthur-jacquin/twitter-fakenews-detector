from pytest import *
from credibility.credibility_analysis import ml_analysis
from twitter.collector import collect_tweets,transform_to_dataframe

def test_ml_analysis():
    tweet = collect_tweets('trump',1)
    data = transform_to_dataframe(tweet)
    text = data['tweet_textual_content']
    pred = ml_analysis(text)
    assert 0 <= pred
    assert pred <= 1

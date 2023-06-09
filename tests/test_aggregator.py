from credibility.aggregator import credibility
from twitter.collector import transform_to_dataframe, collect_tweets


for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_aggregator():
    final_grade = credibility(tweet)[0]
    assert 0 <= final_grade
    assert final_grade <= 1

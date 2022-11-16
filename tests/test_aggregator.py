from credibility.aggregator import credibility, force_0_1, barycentre
from twitter.collector import transform_to_dataframe, collect_tweets


for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_aggregator():
    final_grade = credibility(tweet)[0]
    assert 0 <= final_grade
    assert final_grade <= 1


def test_utils():
    assert force_0_1(-.2) == 0
    assert force_0_1(.5) == .5
    assert force_0_1(1.3) == 1

    assert barycentre([(0, 1), (1, 3)]) == .75

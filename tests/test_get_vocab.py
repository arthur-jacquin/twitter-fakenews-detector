from twitter.collector import collect_tweets, transform_to_dataframe
from deep_analysis.get_vocab import get_vocab

for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_get_vocab():
    assert type(get_vocab(tweet)) == str
    assert get_vocab(tweet) != ""

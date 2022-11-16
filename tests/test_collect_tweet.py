from twitter.collector import collect_tweets


def test_collect_tweets():
    tweet = collect_tweets("trump", 3)
    assert tweet[0] != []
    assert tweet[1] != []
    assert tweet[2] != []
    assert tweet[3] != []
    assert tweet[4] != []
    assert tweet[5] != []
    assert tweet[6] != []
    assert tweet[7] != []

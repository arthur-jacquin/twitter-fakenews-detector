from deep_analysis.sentiment_analysis import sentiment_analysis
from twitter.collector import transform_to_dataframe, collect_tweets

for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_sentiment_analysis():
    assert (sentiment_analysis(tweet)[0] >= 0 and sentiment_analysis(tweet)[0] <= 1
            and sentiment_analysis(tweet)[1] >= 0 and sentiment_analysis(tweet)[1] <= 1)

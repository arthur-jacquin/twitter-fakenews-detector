from credibility.profile_analysis import account_age, number_of_followers, number_of_following, ratio_of_statuses_account_age
from twitter.collector import transform_to_dataframe, collect_tweets

for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_account_age():
    assert type(account_age(tweet)) == float


def test_number_of_followers():
    assert type(number_of_followers(tweet)) == int


def test_number_of_following():
    assert type(number_of_following(tweet)) == int


def test_ratio_of_statuses_account_age():
    assert type(ratio_of_statuses_account_age(tweet)) == float


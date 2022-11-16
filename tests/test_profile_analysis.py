from credibility.profile_analysis import account_age, number_of_followers, number_of_following, ratio_of_statuses_account_age
from twitter.collector import transform_to_dataframe, collect_tweets

# def test_account_age():
#    pass

for _, row in transform_to_dataframe(collect_tweets('trump', 1)).iterrows():
    tweet = row


def test_number_of_followers():
    assert type(number_of_followers(tweet)) == int


test_number_of_followers()

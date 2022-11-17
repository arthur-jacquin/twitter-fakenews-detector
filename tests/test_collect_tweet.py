from twitter.collector import collect_tweets, get_rt_author_info, transform_to_dataframe, get_tweet_info, get_user_info


def test_transform_to_dataframe():
    assert transform_to_dataframe({'answer': [42]}).empty == False


def test_collect_tweets():
    tweets = collect_tweets("trump", 3)

    assert 'tweet_textual_content' in tweets
    assert 'user_id' in tweets
    assert 'tweet_id' in tweets
    assert 'user_creation_date' in tweets
    assert 'tweet_nb_rt' in tweets
    assert 'user_nb_followers' in tweets
    assert 'user_nb_followings' in tweets
    assert 'user_nb_status' in tweets


def test_get_rt_author_info():
    info = get_rt_author_info(1590478616638689280, 3)

    assert 'user_creation_date' in info
    assert 'user_nb_followers' in info
    assert 'user_nb_followings' in info
    assert 'user_nb_status' in info


def test_get_tweet_info():
    tweet = get_tweet_info(1592765408754311168)

    assert 'tweet_textual_content' in tweet
    assert 'user_id' in tweet
    assert 'tweet_id' in tweet
    assert 'user_creation_date' in tweet
    assert 'tweet_nb_rt' in tweet
    assert 'user_nb_followers' in tweet
    assert 'user_nb_followings' in tweet
    assert 'user_nb_status' in tweet


def test_get_user_info():
    user = get_user_info("lecartographe")

    assert 'user_creation_date' in user
    assert 'user_nb_followers' in user
    assert 'user_nb_followings' in user
    assert 'user_nb_status' in user

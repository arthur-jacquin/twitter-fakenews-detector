from twitter.connection_setup import twitter_setup
import tweepy


def test_connection_setup():
    assert twitter_setup() != None

from twitter.connection_setup import twitter_setup
import tweepy
from pytest import *


def test_connection_setup():
    assert twitter_setup() != None

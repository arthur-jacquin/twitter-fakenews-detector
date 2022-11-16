from twitter.connection_setup import twitter_setup
import tweepy
from pytest import *

assert twitter_setup() != None

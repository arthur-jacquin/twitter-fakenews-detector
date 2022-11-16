from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq
import matplotlib.pyplot as plt
from credibility.aggregator import credibility
from twitter.collector import collect_tweets,transform_to_dataframe


def topic_analysis(queries, tweet_number):
    '''
    Compute the analysis of the query, return a DASH element.
    '''
    Credibility_index = []
    Tweets = []
    data = collect_tweets(queries,tweet_number)
    data = transform_to_dataframe(data)
    for _, row in data.iterrows():
        Tweets.append(row)
    for i in range(len(Tweets)):
        Credibility_index.append(credibility(Tweets[i]))
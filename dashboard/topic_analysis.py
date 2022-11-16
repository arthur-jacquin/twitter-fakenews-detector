from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq
import re
from credibility.aggregator import credibility
from twitter.collector import collect_tweets,transform_to_dataframe


def topic_analysis(queries, tweet_number):
    '''
    Compute the analysis of the query, return a DASH element.
    '''
    #Séparation en sous-requêtes
    Queries = re.split('/n',queries)
    Credibility_index = []
    Tweets = []
    for k in range(len(Queries)):
        data = collect_tweets(Queries[k],tweet_number)
        data = transform_to_dataframe(data)
        for _, row in data.iterrows():
            Tweets.append(row)
    for i in range(len(Tweets)):
        Credibility_index.append(credibility(Tweets[i]))
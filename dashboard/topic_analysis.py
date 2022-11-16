from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq
import re
from credibility.aggregator import credibility
from twitter.collector import collect_tweets,transform_to_dataframe
import numpy as np




def topic_analysis(queries, tweet_number):
    '''
    Compute the analysis of the query, return a DASH element.
    '''
    #Séparation en sous-requêtes
    Queries = re.split('/n',queries)

    for k in range(len(Queries)):
        data = collect_tweets(Queries[k],tweet_number)
        data = transform_to_dataframe(data)
        Credibility_index = []
        Tweets = []
        for _, row in data.iterrows():
            Tweets.append(row)
        for i in range(len(Tweets)):
            Credibility_index.append(credibility(Tweets[i]))

    A=[]
    for i in range(3):
        p=np.min(Credibility_index)
        j=0
        while Credibility_index[j]!=p:
            j+=1
        A.append(Tweets[j],Credibility_index[j])
        Tweets=Tweets[:j]+ Tweets[j+1:]
        Credibility_index=Credibility_index[:j]+ Credibility_index[j+1:]
    


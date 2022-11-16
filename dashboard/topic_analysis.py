from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq
import matplotlib.pyplot as plt
from credibility.aggregator import credibility
from twitter.collector import collect_tweets,transform_to_dataframe
import numpy as np




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
    
    Tweets2=np.copy(Tweets)
    Credibility_index2=np.copy(Credibility_index)    #On modifie les 2 listes copiées

    A=[];B=[]      #A est la liste des 3 pires tweets et B les trois meilleurs , c'est des listes de tuples (Tweet, crédibilité)
    for i in range(3):
        p=np.min(Credibility_index2)
        j=0
        while Credibility_index2[j]!=p:
            j+=1
        A.append((Tweets[j],Credibility_index2[j]))
        Tweets2=Tweets2[:j]+ Tweets2[j+1:]
        Credibility_index2=Credibility_index2[:j]+ Credibility_index2[j+1:]
    for i in range(3):
        p=np.max(Credibility_index2)
        j=0
        while Credibility_index2[j]!=p:
            j+=1
        B.append((Tweets2[j],Credibility_index2[j]))
        Tweets2=Tweets2[:j]+ Tweets2[j+1:]
        Credibility_index2=Credibility_index2[:j]+ Credibility_index2[j+1:]

    #Histogramme
    histo = dcc.Graph(figure=plt.hist(Credibility_index))

    return 
    
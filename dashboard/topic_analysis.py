from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq

def topic_analysis(queries, tweet_number):
    '''
    Compute the analysis of the query, return a DASH element.
    '''

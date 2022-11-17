from deep_analysis.sentiment_analysis import sentiment_analysis
from twitter.collector import get_rt_author_info, transform_to_dataframe
from credibility.aggregator import author_credibility

from dash import dcc, html
import pandas as pd


def html_of_tweet(tweet, cred, info, folded=True, NB_RT=100):
    '''
    Display a tweet.

    Folded mode: textual content, author name.
    Added in unfolded mode:
    - credibility (colored score)
        - machine learning model (colored score)
        - author credibility (colored score)
            - account age (value, colored score)
            - following/followers ratio (value, colored score)
            - activity (value, colored score)
    - virality (value)
    - polarity (value, description)
    - subjectivity (value, description)
    - retweeters credibility repartition
    '''
    # Extract informations
    content = tweet['tweet_textual_content']
    author = tweet['user_name']
    ml_score = info['ml']
    author_cred = info['author'][0]
    age, age_cred = info['author'][1]['age']
    activity, activity_cred = info['author'][1]['activity']
    follow, follow_cred = info['author'][1]['follow']
    rt = tweet['tweet_nb_rt']
    polarity, subjectivity = sentiment_analysis(tweet)

    # Extract retweeters credibility
    df = transform_to_dataframe(get_rt_author_info(tweet['tweet_id'], NB_RT))
    rt_cred = []
    for _, tweet in df.iterrows():
        author_cred, _ = author_credibility(tweet)
        rt_cred.append(author_cred)

    # DASH results
    # TODO
    return html.Div([
        html.Div(content, className="tweet"),
        html.Div(
            f"Posted by @{author}, got {rt} retweets, credibility index of {cred}.")
    ])


def parse_user_input(input):
    if input[:4] == "http":
        input = (input.split('/')[-1]).split('?')[0]
    return int(input)

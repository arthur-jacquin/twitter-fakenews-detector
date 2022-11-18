""" Compute a tweet analysis display. """

from dash import dcc, html
import pandas as pd
import plotly.express as px

from deep_analysis.sentiment_analysis import sentiment_analysis
from twitter.collector import get_rt_author_info, transform_to_dataframe, get_tweet_info
from credibility.aggregator import author_credibility, credibility
from dashboard.utils import to_li_item, format_age, format_activity

COLOR = px.colors.sequential.RdBu
NB_RT = 100


def html_of_tweet(tweet, cred, info, rt_exploration=False, folded=True):
    """ Compute the analysis of the tweet.

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

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.
    cred : float
        Credibility of the tweet.
    info : dict
        Additionnal informations on the credibility analysis.
    folded : bool (optionnal, defaults to True)
        Decide wether advanced analytics are displayed directly.

    Returns
    -------
    DASH element
        The topic analysis.
    """

    # Extract informations
    content = tweet['tweet_textual_content']
    author = tweet['user_name']
    ml_score = info['ml']
    author_cred = info['author'][0]
    age, age_cred = info['author'][1]['age']
    activity, activity_cred = info['author'][1]['activity']
    follow, follow_cred = info['author'][1]['follow']
    nb_rt = tweet['tweet_nb_rt']
    polarity, subjectivity = sentiment_analysis(tweet)

    # DASH results
    res = [
        html.Summary(f'Tweeted by @{author}.'),
        html.Ul(children=[
            to_li_item('Credibility', score=cred),
            html.Ul(children=[
                to_li_item('Machine learning-based estimation',
                           score=ml_score),
                to_li_item('Author credibility', score=author_cred),
                html.Ul(children=[
                    to_li_item('Account age',
                        value=format_age(age),
                        score=age_cred),
                    to_li_item('Following/followers ratio',
                        value=str(round(follow, 2)),
                        score=follow_cred),
                    to_li_item('Activity',
                        value=format_activity(activity),
                        score=activity_cred),
                ]),
            ]),
            to_li_item('Virality', value=f'{nb_rt} retweets'),
            to_li_item('Polarity', value=str(round(polarity, 2)),
                       description='(-1: negative, 1: positive)'),
            to_li_item('Subjectivity', value=str(round(subjectivity, 2)),
                       description='(0: objective, 1: subjective)'),
            to_li_item('Tweet ID', value=str(tweet['tweet_id']),
                       description='(use it in the "Tweet analysis" tab)'),
        ]),
    ]

    if rt_exploration:
        # Extract retweeters credibility
        dataframe = transform_to_dataframe(
            get_rt_author_info(tweet['tweet_id'], NB_RT))
        rt_cred = []
        for _, retweet in dataframe.iterrows():
            author_cred, _ = author_credibility(retweet)
            rt_cred.append(author_cred)
        res += [dcc.Graph(figure=px.histogram(
            pd.DataFrame({'retweets': rt_cred}),
            x="retweets",
            color_discrete_sequence=COLOR,
        ))]

    return html.Div(className='tweet', children=[
        html.Div(content, className='tweet_content'),
        html.Details(open=not (folded), children=res),
    ])


def parse_tweet_input(_input):
    """ Parse tweet input.

    Parameters
    ----------
    _input : string
        Tweet ID or sharing URL.

    Returns
    -------
    int
        Tweet ID.
    """
    if _input[:4] == "http":
        _input = (_input.split('/')[-1]).split('?')[0]
    return int(_input)


def html_of_tweet_id(tweet_id):
    """ Compute the analysis of the tweet.

    See html_of_tweet.

    Parameters
    ----------
    tweet_id : int
        Tweet ID.

    Returns
    -------
    DASH element
        The topic analysis.
    """

    tweet = get_tweet_info(tweet_id)
    cred, info = credibility(tweet)
    return [html.H2('Results'), html_of_tweet(tweet, cred, info, rt_exploration=True, folded=False)]

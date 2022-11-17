from deep_analysis.sentiment_analysis import sentiment_analysis
from twitter.collector import get_rt_author_info, transform_to_dataframe, get_tweet_info
from credibility.aggregator import author_credibility, credibility
from dashboard.utils import format_age, format_activity

from dash import dcc, html
import pandas as pd
import plotly.express as px

COLOR = px.colors.sequential.RdBu


def to_li_item(name, value=None, score=None, description=None):
    res = [html.Span(name, className='category')]
    if value:
        res.append(html.Span(value, className='value'))
    if description:
        res.append(html.Span(description, className='description'))
    if score:
        res.append(html.Span(str(round(score, 2)), className='score'))
    return html.Li(children=res)


def html_of_tweet(tweet, cred, info, folded=True, NB_RT=20):
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
    rt_fig = px.histogram(
        pd.DataFrame({'retweets': rt_cred}),
        x="retweets",
        color_discrete_sequence=COLOR,
    )

    # DASH results
    return html.Div(className='tweet', children=[
        html.Div(content, className='tweet_content'),
        html.Div(f'Tweeted by @{author}', className='tweet_author'),
        html.Details(open=not (folded), children=[
            html.Summary('Show/hide analysis breakdown'),
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
                            value=round(follow, 2),
                            score=follow_cred),
                        to_li_item('Activity',
                            value=format_activity(activity),
                            score=activity_cred),
                    ]),
                ]),
                to_li_item('Virality', value=f'{rt} retweets'),
                to_li_item('Polarity', value=f'{round(polarity, 2)}',
                           description='(-1: negative, 1: positive)'),
                to_li_item('Subjectivity', value=f'{round(subjectivity, 2)}',
                           description='(0: ojbective, 1: subjective)'),
                to_li_item('Retweeters credibility repartition')
            ]),
            dcc.Graph(figure=rt_fig),
        ]),
    ])


def parse_user_input(input):
    if input[:4] == "http":
        input = (input.split('/')[-1]).split('?')[0]
    return int(input)


def html_of_tweet_id(id):
    tweet = get_tweet_info(id)
    cred, info = credibility(tweet)
    return [html.H2('Results'), html_of_tweet(tweet, cred, info, folded=False)]

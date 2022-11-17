""" Fake News Detector.

See the README.md for more informations.

Create and launch a web server hosting the Fake News Detector web app.
"""

from dash import Dash, dcc, html, Input, Output, State

from dashboard.topic_analysis import topic_analysis
from dashboard.tweet_analysis import parse_tweet_input, html_of_tweet_id
from dashboard.user_analysis import parse_user_input, html_of_user_id

app = Dash(__name__)

app.layout = html.Div([

    # Title
    html.H1('Twitter analysor'),

    # Ecological banner
    html.Div(id='ecology', children=[
        html.H3('Be aware of your environmental impact!'),
        html.P('This application queries Twitter servors and process some tweets.'),
        html.P('While the power consumption of Twitter servors can not be known, \
            the CarbonAI package will measure the power consumption of our server. \
            The higher the number of tweets, the higher the consumption. Please pay attention ;)'),
        html.P('The processing also use a machine-learning model that took  to train.'),
    ]),

    dcc.Tabs([
        # Topic analysis
        dcc.Tab(label='Topic analysis', children=[
            html.H2('Query'),
            html.H3('Topics'),
            html.P('Please enter keywords (a query will be made for each line).'),
            dcc.Textarea(
                id='text-input',
                value='biden\ntrump',
                style={'width': '100%', 'height': 60},
            ),
            html.H3('Number of tweets to fetch'),
            dcc.Slider(1, 3, 0.01, value=1, id='slider', marks={
                       i: str(10**i) for i in range(1, 4)}),
            html.Button('Submit', id='submit-button', n_clicks=0),

            html.Div(id='analysis')
        ]),

        # User analysis
        dcc.Tab(label='User analysis', children=[
            html.H2('Query'),
            html.P('Please enter an username or a profile-page URL.'),
            dcc.Input(id="user-input", type="text"),
            html.Button('Submit', id='user-submit-button', n_clicks=0),

            html.Div(id='user-analysis')
        ]),

        # Tweet analysis
        dcc.Tab(label='Tweet analysis', children=[
            html.H2('Query'),
            html.P('Please enter the ID or the sharing URL of a tweet.'),
            dcc.Input(id="tweet-input", type="text"),
            html.Button('Submit', id='tweet-submit-button', n_clicks=0),

            html.Div(id='tweet-analysis')
        ]),
    ]),
])


@app.callback(
    Output('analysis', 'children'),
    Input('submit-button', 'n_clicks'),
    State('text-input', 'value'),
    State('slider', 'value'),
)
def update_output_topic(n_clicks, queries, tweet_number_linear):
    """ Generate and return the topic analysis

    Parameters
    ----------
    n_clicks : int
        The number of time the submit button has been clicked.
    queries : string
        The query written by the user in the input area.
    tweet_number_linear: float
        The logarithm of the number of tweets to fetch.

    Returns
    -------
    DASH element
        The topic analysis.
    """
    tweet_number = int(10**(tweet_number_linear))
    if n_clicks > 0 and queries:
        return topic_analysis(queries, tweet_number)
    return None


@app.callback(
    Output('user-analysis', 'children'),
    Input('user-submit-button', 'n_clicks'),
    State('user-input', 'value'),
)
def update_output_user(n_clicks, user):
    """ Generate and return the user analysis

    Parameters
    ----------
    n_clicks : int
        The number of time the submit button has been clicked.
    user : string
        The user name or profile-page URL written by the user.

    Returns
    -------
    DASH element
        The user analysis.
    """
    if n_clicks > 0 and user:
        return html_of_user_id(parse_user_input(user))
    return None


@app.callback(
    Output('tweet-analysis', 'children'),
    Input('tweet-submit-button', 'n_clicks'),
    State('tweet-input', 'value'),
)
def update_output_tweet(n_clicks, tweet):
    """ Generate and return the tweet analysis

    Parameters
    ----------
    n_clicks : int
        The number of time the submit button has been clicked.
    tweet : string
        The id or sharing URL of a tweet.

    Returns
    -------
    DASH element
        The tweet analysis.
    """
    if n_clicks > 0 and tweet:
        return html_of_tweet_id(parse_tweet_input(tweet))
    return None


if __name__ == '__main__':
    app.run_server(debug=True)

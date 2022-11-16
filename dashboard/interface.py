from dashboard.topic_analysis import topic_analysis

from dash import Dash, dcc, html, Input, Output, State
import dash_daq as daq

app = Dash(__name__)

app.layout = html.Div([

    # Title
    html.H1('Twitter analysor'),


    # Input area
    html.H3('Topics'),
    dcc.Textarea(
        id='text-input',
        value='biden\ntrump',
        style={'width': '100%', 'height': 60},
    ),

    html.H3('Number of tweets to fetch'),
    dcc.Slider(0, 100, value=10, id='slider'),

    html.Button('Submit', id='submit-button', n_clicks=0),


    # Analysis
    html.Div(id='analysis')
])


@app.callback(
    Output('analysis', 'children'),
    Input('submit-button', 'n_clicks'),
    State('text-input', 'value'),
    State('slider', 'value'),
)
def update_output(n_clicks, queries, tweet_number):
    if n_clicks > 0:
        return topic_analysis(queries, tweet_number)


if __name__ == '__main__':
    app.run_server(debug=True)

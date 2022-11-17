from credibility.aggregator import credibility
from deep_analysis.sentiment_analysis import sentiment_analysis
from twitter.collector import collect_tweets, transform_to_dataframe

from dash import dcc, html
import pandas as pd
import plotly.express as px

COLOR = px.colors.sequential.RdBu


def html_of_tweet(tweet, cred, comment):
    content = tweet['tweet_textual_content']
    author = tweet['user_name']
    rt = tweet['tweet_nb_rt']
    return html.Div([
        html.Div(content, className="tweet"),
        html.Div(
            f"Posted by @{author}, got {rt} retweets, credibility index of {cred}.")
    ])


def topic_analysis(queries, tweet_number):
    '''
    Compute the analysis of the query, return a DASH element.
    '''
    # Collect tweets
    df = transform_to_dataframe(collect_tweets(queries, tweet_number))

    # Process tweets
    creds = []
    comments = []
    polarities = []
    subjectivities = []
    tweets = []
    rts = []
    for _, tweet in df.iterrows():
        tweets.append(tweet)
        cred, comment = credibility(tweet)
        creds.append(cred)
        comments.append(comment)
        polarity, subjectivity = sentiment_analysis(tweet)
        polarities.append(polarity)
        subjectivities.append(subjectivity)
        rts.append(tweet['tweet_nb_rt'])

    # Sort by credibility
    cred_sorted = [(creds[i], i) for i in range(len(creds))]
    cred_sorted.sort()

    # Preparation before updating
    res = [html.H2('Results')]

    # Credibility-virality correlation
    res.append(html.H3('Credibility-virality correlation'))
    cred_virality_fig = px.density_heatmap(
        pd.DataFrame({
            'credibility': creds,
            'virality': rts,
        }),
        x='credibility', y='virality',
        # range_x=[0., 1.], range_y=[0., max(rts)],
        marginal_x="histogram", marginal_y="histogram",
        color_continuous_scale=COLOR,
    )
    res.append(dcc.Graph(figure=cred_virality_fig))

    # Tweet selection
    res.append(html.H3('Tweet selection'))
    res.append(html.H4('Most trustable tweets'))
    for i in [cred_sorted[j][1] for j in range(3)]:
        res.append(html_of_tweet(tweets[i], creds[i], comments[i]))
    res.append(html.H4('Least trustable tweets'))
    for i in [cred_sorted[j][1] for j in range(-1, -4, -1)]:
        res.append(html_of_tweet(tweets[i], creds[i], comments[i]))

    # Credibility-polarity correlation
    res.append(html.H3('Credibility-polarity correlation'))
    cred_polarity_fig = px.density_heatmap(
        pd.DataFrame({
            'credibility': creds,
            'polarity': polarities,
        }),
        x='credibility', y='polarity',
        # range_x=[0., 1.], range_y=[0., max(rts)],
        marginal_x="histogram", marginal_y="histogram",
        color_continuous_scale=COLOR,
    )
    res.append(dcc.Graph(figure=cred_polarity_fig))

    # Credibility-subjectivity correlation
    res.append(html.H3('Credibility-subjectivity correlation'))
    cred_subjectivity_fig = px.density_heatmap(
        pd.DataFrame({
            'credibility': creds,
            'subjectivity': subjectivities,
        }),
        x='credibility', y='subjectivity',
        # range_x=[0., 1.], range_y=[0., max(rts)],
        marginal_x="histogram", marginal_y="histogram",
        color_continuous_scale=COLOR,
    )
    res.append(dcc.Graph(figure=cred_subjectivity_fig))

    return res

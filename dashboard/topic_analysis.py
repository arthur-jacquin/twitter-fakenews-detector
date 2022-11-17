""" Compute a topic analysis display """

from io import BytesIO
import base64

from dash import dcc, html
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud

from credibility.aggregator import credibility
from deep_analysis.sentiment_analysis import sentiment_analysis
from deep_analysis.get_vocab import get_vocab
from twitter.collector import collect_tweets, transform_to_dataframe
from dashboard.tweet_analysis import html_of_tweet

COLOR = px.colors.sequential.RdBu


def topic_analysis(queries, tweet_number):
    """ Compute the analysis of the query.

    Parameters
    ----------
    queries : string
        The query written by the user in the input area.
    tweet_number : int
        The number of tweets to fetch.

    Returns
    -------
    DASH element
        The topic analysis.
    """

    # Collect tweets
    dataframe = transform_to_dataframe(collect_tweets(queries, tweet_number))

    # Process tweets
    creds = []
    infos = []
    polarities = []
    subjectivities = []
    tweets = []
    rts = []
    for _, tweet in dataframe.iterrows():
        tweets.append(tweet)
        cred, info = credibility(tweet)
        creds.append(cred)
        infos.append(info)
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
        marginal_x="histogram", marginal_y="histogram",
        color_continuous_scale=COLOR,
    )
    res.append(dcc.Graph(figure=cred_virality_fig))

    # Tweet selection
    res.append(html.H3('Tweet selection'))
    res.append(html.H4('Most trustable tweets'))
    for i in [cred_sorted[j][1] for j in range(3)]:
        res.append(html_of_tweet(tweets[i], creds[i], infos[i]))
    res.append(html.H4('Least trustable tweets'))
    for i in [cred_sorted[j][1] for j in range(-1, -4, -1)]:
        res.append(html_of_tweet(tweets[i], creds[i], infos[i]))

    # Credibility-polarity correlation
    res.append(html.H3('Credibility-polarity correlation'))
    cred_polarity_fig = px.density_heatmap(
        pd.DataFrame({
            'credibility': creds,
            'polarity': polarities,
        }),
        x='credibility', y='polarity',
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
        marginal_x="histogram", marginal_y="histogram",
        color_continuous_scale=COLOR,
    )
    res.append(dcc.Graph(figure=cred_subjectivity_fig))

    # Related words
    res.append(html.H3('Related vocabulary'))
    vocab = ''
    number_of_fetched_tweets = len(tweets)
    for i in range(int(0.7*number_of_fetched_tweets), number_of_fetched_tweets):
        vocab += get_vocab(tweets[i]) + ' '
    wordcloud_img = WordCloud(max_font_size=40).generate(vocab).to_image()
    img = BytesIO()
    wordcloud_img.save(img, format='PNG')
    res.append(html.Img(
        src=f'data:image/png;base64,{base64.b64encode(img.getvalue()).decode()}'))

    return res

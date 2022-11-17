from credibility.aggregator import author_credibility
from twitter.collector import get_user_info
from dashboard.utils import to_li_item, format_activity, format_age

from dash import html


def parse_user_input(input):
    if input[:4] == "http":
        input = input.split('/')[-1]
    return input


def html_of_user_id(user_id):
    '''
    Estimate the credibility of an user, return a DASH element.
    '''
    # Get user
    user = get_user_info(user_id)

    # Compute credibility, extract results
    author_cred, info = author_credibility(user)
    age, age_cred = info['age']
    activity, activity_cred = info['activity']
    follow, follow_cred = info['follow']

    # DASH results
    return html.Div(children=[
        html.H2('Results'),
        html.Ul(children=[
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
    ])

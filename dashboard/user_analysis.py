""" Compute a user analysis display. """

from dash import html

from credibility.aggregator import author_credibility
from twitter.collector import get_user_info
from dashboard.utils import to_li_item, format_activity, format_age


def parse_user_input(_input):
    """ Parse user input.

    Parameters
    ----------
    _input : string
        User name or profile-page URL.

    Returns
    -------
    int
        User ID.
    """
    if _input[:4] == "http":
        _input = _input.split('/')[-1]
    return _input


def html_of_user_id(user_id):
    """ Compute the analysis of the user.

    Parameters
    ----------
    user_id : int
        User ID.

    Returns
    -------
    DASH element
        The user analysis.
    """

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

""" Tools for dashboard package. """

from dash import html


def to_li_item(name, value=None, score=None, description=None):
    """ Format data to a li DASH component.

    Parameters
    ----------
    name : string
        Title of component.
    value : string (optionnal)
        Value of component.
    score : float (optionnal)
        Score of component.
    description : string (optionnal)
        description of component.

    Returns
    -------
    li DASH element
        The asssociated element.
    """

    res = [html.Span(name, className='category')]
    if value:
        res.append(html.Span(value, className='value'))
    if description:
        res.append(html.Span(description, className='description'))
    if score:
        # Coloration
        res.append(html.Span(str(round(score, 2)), className='score'))
    return html.Li(children=res)


def barycentre(points):
    """ Compute a weighted average.

    Parameters
    ----------
    points : list of (point, weight)
        point must be a float between 0 and 1.

    Returns
    -------
    float
        The weighted average.
    """

    res = 0
    ponderation = 0

    for point, pond in points:
        res += point*pond
        ponderation += pond

    return res/ponderation


def force_0_1(t):
    """ Force a float to be between 0 and 1. """
    return min(max(0, t), 1)


def format_age(age):
    return age


def format_activity(activity):
    return activity

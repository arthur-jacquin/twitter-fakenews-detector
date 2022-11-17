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
    if value != None:
        res.append(html.Span(value, className='value'))
    if description != None:
        res.append(html.Span(description, className='description'))
    if score != None:
        if score >= 0.8:
            class_name = 'score_bad'
        elif score <= 0.5:
            class_name = 'score_good'
        else:
            class_name = 'score_neutral'
        res.append(html.Span(str(round(score, 2)), className=class_name))
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
    """ Format an age.

    Parameters
    ----------
    age : float
        Number of seconds.

    Returns
    -------
    string
        Formatted age.
    """

    if age < 3600*24:  # Less than a day old
        return f'{int(age/3600)} hour(s)'
    elif age < 3600*24*30:  # Less than a month old
        return f'{int(age/(3600*24))} day(s)'
    elif age < 3600*24*30*12:  # Less than a year old
        return f'{int(age/(3600*24*30))} month(s)'
    else:
        return f'{int(age/(3600*24*365))} year(s)'


def format_activity(activity):
    """ Format an activity.

    Parameters
    ----------
    activity : float
        Number of seconds.

    Returns
    -------
    string
        Formatted activity.
    """

    statuses_per_day = activity*3600*24

    if statuses_per_day > 1:  # More than once a day
        return f'{int(statuses_per_day)} status(es) per day'
    elif 30*statuses_per_day > 1:  # More than once a month
        return f'{int(statuses_per_day*30)} status(es) per month'
    elif 365*statuses_per_day > 1:  # More than once a year
        return f'{int(statuses_per_day*365)} status(es) per year'
    else:
        return 'Less than once a year'

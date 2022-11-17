from dash import html


def to_li_item(name, value=None, score=None, description=None):
    res = [html.Span(name, className='category')]
    if value:
        res.append(html.Span(value, className='value'))
    if description:
        res.append(html.Span(description, className='description'))
    if score:
        res.append(html.Span(str(round(score, 2)), className='score'))
    return html.Li(children=res)


def barycentre(points):
    '''
    Renvoie un barycentre de points
    Input: liste de (point dans [0; 1], pondération)
    Output: barycentre des points pondérés
    '''
    res = 0
    ponderation = 0

    for point, pond in points:
        res += point*pond
        ponderation += pond

    return res/ponderation


def force_0_1(t):
    ''' Map t between 0 and 1 '''
    return min(max(0, t), 1)


def format_age(age):
    return age


def format_activity(activity):
    return activity

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

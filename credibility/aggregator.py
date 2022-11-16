import numpy as np
from math import log
from credibility.credibility_analysis import ml_analysis
from credibility.profile_analysis import account_age, number_of_followers, number_of_following, ratio_of_statuses_account_age


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


def author_credibility(tweet):
    '''
    Compute a real between 0 and 1 reflecting the credibility of the tweet author.
    The higher the number is, the most suspicious the author is.

    Also returns the breakdown analysis, as well as some alerts and indications.
    '''
    # Account age
    # Moins d'un mois: ça craint; Plus d'un an: ok
    age_credibility = force_0_1(
        1 - log(account_age(tweet)/(24*3600*30))/log(12))

    # Ratio status/age du compte
    # Plus d'un tweet par heure: ça craint; Moins d'un par jour: ok
    activity_credibility = force_0_1(
        log(ratio_of_statuses_account_age(tweet)*(24*3600))/log(24))

    # Ratio follower/following
    # Moins de 10 followers ou ratio >= 10: ça craint; ratio <= 2: ok
    if number_of_followers(tweet) <= 10 or number_of_following(tweet) <= 10:
        follow_credibility = 1
    else:
        # number_of_follow{ers, ing}(tweet) != 0 because > 10
        ratio = number_of_following(tweet)/number_of_followers(tweet)
        if ratio == 0:
            follow_credibility
        follow_credibility = force_0_1(log(ratio/2)/log(10/2))

    return barycentre([
        (age_credibility, 1),
        (activity_credibility, 1),
        (follow_credibility, 1),
    ]), None


def credibility(tweet):
    '''
    Compute a real between 0 and 1 reflecting the credibility of a tweet.
    The higher the number is, the most likely the tweet is fake news.

    Also returns the breakdown analysis, as well as some alerts and indications.
    '''
    # Machine learning
    ml_credibility = force_0_1(ml_analysis(tweet))

    # Author
    author_cred, info = author_credibility(tweet)

    return barycentre([
        (ml_credibility, 4),
        (author_cred, 1),
    ]), None

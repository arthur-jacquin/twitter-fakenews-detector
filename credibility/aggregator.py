""" Aggregates information to compute an unique credibility estimation. """

from math import log

from credibility.credibility_analysis import ml_analysis
from credibility.profile_analysis import account_age, number_of_followers, number_of_following, ratio_of_statuses_account_age
from dashboard.utils import barycentre, force_0_1


def author_credibility(tweet):
    """ Compute the credibility of the tweet author.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    float
        The estimated credibility, between 0 and 1.
        The higher the number is, the most suspicious the author is.
    dict
        Analysis breakdown.
    """

    # Account age
    # Moins d'un mois: ça craint; Plus d'un an: ok
    age = account_age(tweet)
    age_credibility = force_0_1(
        1 - log(age/(24*3600*30))/log(12))

    # Ratio status/age du compte
    # Plus d'un tweet par heure: ça craint; Moins d'un par jour: ok
    activity = ratio_of_statuses_account_age(tweet)
    activity_credibility = force_0_1(
        log(activity*(24*3600))/log(24))

    # Ratio follower/following
    # Moins de 10 followers ou ratio >= 10: ça craint; ratio <= 2: ok
    if number_of_followers(tweet) <= 10 or number_of_following(tweet) <= 10:
        ratio = 0
        follow_credibility = 1
    else:
        # number_of_follow{ers, ing}(tweet) != 0 because > 10
        ratio = number_of_following(tweet)/number_of_followers(tweet)
        follow_credibility = force_0_1(log(ratio/2)/log(10/2))

    return barycentre([
        (age_credibility, 1),
        (activity_credibility, 1),
        (follow_credibility, 1),
    ]), {
        'age': (age, age_credibility),
        'activity': (activity, activity_credibility),
        'follow': (ratio, follow_credibility),
    }


def credibility(tweet):
    """ Compute the credibility of the tweet.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet to analyse.

    Returns
    -------
    float
        The estimated credibility, between 0 and 1.
        The higher the number is, the most likely the tweet is fake news.
    dict
        Analysis breakdown.
    """

    # Machine learning
    ml_credibility = force_0_1(ml_analysis(tweet))

    # Author
    author_cred, info = author_credibility(tweet)

    return barycentre([
        (ml_credibility, 2),
        (author_cred, 1),
    ]), {
        'ml': ml_credibility,
        'author': (author_cred, info),
    }

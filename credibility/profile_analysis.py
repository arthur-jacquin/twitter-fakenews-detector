
def age_compte(tweet):
    """
    Cette fonction renvoie l'age du compte
    qui a tweeté un tweet
    :return: int : l'age du compte en jours
    """
    return tweet.user.created_at

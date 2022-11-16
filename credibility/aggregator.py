import numpy as np
import math
from credibility.credibility_analysis import ml_analysis
from credibility.profile_analysis import account_age, number_of_followers, number_of_following, ratio_of_statuses_account_age


"""
Liste des coefficients, modifiable, dans l'ordre :
- ML
- age compte
- ratio publi/age
- ratio follows/followers """
coeff = np.array([0.2,0.2,0.2,0.2,0.1,0.1])
assert coeff.sum() == 1 

def credibility(tweet):
    '''
    Compute a real between 0 and 1 reflecting the credibility of a tweet.
    The higher the number is, the most likely the tweet is fake news.
    '''
    return ml_analysis(tweet)*coeff[0,0] + coeff[0,1]/math.log(account_age(tweet)) + coeff[0,2]*ratio_of_statuses_account_age(tweet) + coeff[0,3]*number_of_following(tweet)/number_of_followers(tweet)

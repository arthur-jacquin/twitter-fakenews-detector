from textblob import TextBlob
from textblob import Word

import nltk
nltk.download('omw-1.4')


def get_vocab(tweet):
    '''This function returns a string with only the important words contained in a tweet'''

    vocab = ""
    # Liste de type de mots 'inutile' (déterminants, etc)
    L = ['DT', 'IN', 'PRP', 'PRP$']
    # Loop through rows
    content = tweet['tweet_textual_content']
    tagged = TextBlob(content).tags
    for word, tag in tagged:
        # Lemmatization
        word = Word(word).lemmatize()
        # Some cleaning
        if tag not in L and word != 'http' or word != 'https' and word[0:2] != '//':
            vocab = vocab + " " + word  # concatenating the text
    return vocab

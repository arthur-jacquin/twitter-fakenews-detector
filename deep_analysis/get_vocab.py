""" Vocabulary extraction """

from textblob import TextBlob, Word

MEANINGLESS_WORD_TYPES = ['DT', 'IN', 'PRP', 'PRP$']


def get_vocab(tweet):
    """ Extract the vocabulary of a tweet.

    Parameters
    ----------
    tweet : dataframe row/dict
        Tweet from which extract some vocabulary.

    Returns
    -------
    string
        A concatenation of extracted vocabulary.
    """

    vocab = ""
    content = tweet['tweet_textual_content']
    tagged = TextBlob(content).tags
    for word, tag in tagged:
        # Lemmatization
        word = Word(word).lemmatize()
        # Some cleaning
        if tag not in MEANINGLESS_WORD_TYPES and word[:4] != 'http' and word[:2] != '//':
            vocab += " " + word
    return vocab

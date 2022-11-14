from nltk.stem import WordNetLemmatizer
import re

#Vectorisation d'un tweet
def vectorisation(X):

    """
    Une fonction permettant de pré-traiter une chaîne de caractère dans le but de l'utiliser en entrée d'un classifieur textuel.
    Le pré-traitement consiste en une étape de suppression des caractères spéciaux et des lettres seule, ainsi que le compactage des espaces en des espace de taille 1, puis d'une étape de lemmatisation des mots de la chaîne de caractère 
    
    ----------
    INPUTS

    str (une chaîne de caractère)
    ----------

    ----------
    OUTPUT

    str (une chaîne de caractère pré-traitée)
    ----------

    ----------
    PACKAGES UTILISES

    re
    nltk.stem.WordNetLemmatizer
    ----------
     """


    #Nettoyage du tweet
    documents = []

    stemmer = WordNetLemmatizer()

    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X))
    
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
    
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    
    # Converting to Lowercase
    document = document.lower()
    
    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    
    documents.append(document)
    return documents

def vectorisation_df(df):

    """
    Une fonction permettant de pré-traiter une liste de chaînes de caractères dans le but de l'utiliser en entrée, ou comme dataset d'entraînement/test, d'un classifieur textuel.
    Le pré-traitement consiste en une étape de suppression des caractères spéciaux et des lettres seule, ainsi que le compactage des espaces en des espace de taille 1, puis d'une étape de lemmatisation des mots de la chaîne de caractère 
    
    ----------
    INPUTS

    list(str) (une liste de chaînes de caractère)
    ----------

    ----------
    OUTPUT

    list(str) (une liste de chaînes de caractère pré-traitées)
    ----------

    ----------
    PACKAGES UTILISES

    re
    nltk.stem.WordNetLemmatizer
    ----------
    """
    
    documents = []

    stemmer = WordNetLemmatizer()

    for sen in range(0, len(df)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(df[sen]))
        
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
        
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        
        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        
        # Converting to Lowercase
        document = document.lower()
        
        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        
        documents.append(document)
    return documents
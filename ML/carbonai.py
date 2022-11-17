from tsv_to_txt import Xtrain, Xtest, ytrain, ytest, ytrainraw, ytestraw
from CSV_to_txt import fk, fk_label, lg, lg_label
from vectorisation import vectorisation, vectorisation_df
from carbonai import PowerMeter
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pickle
from sklearn.datasets import load_files
import nltk
nltk.download('stopwords')

power_meter = PowerMeter(project_name="Fake News Detector")


@power_meter.measure_power(
    package="sklearn",
    algorithm="RandomForestClassifier",
    data_type="list",
    data_shape=10000,
    algorithm_params="n_estimators=1000",
    comments="Classifier trained on the MNIST dataset, 3rd test"
)
def my_function():
    # Import du dataset d'entraînement

    # dataset 1
    data_train = load_files(r"..\Dataset_Fake_News_eng\Trainset")
    X_train, y_train = data_train.data, data_train.target

    # dataset 2
    """X_train = fk[0:10001] + lg[0:10001]
   y_train = fk_label[0:10001] + lg_label[0:10001]"""

    # dataset 3
    """X_train = Xtrain
    y_train = ytrain"""

    #############################################################
    # import du dataset de test

    # dataset 1
    data_test = load_files(r"..\Dataset_Fake_News_eng\testing")
    X_test, y_test = data_test.data, data_test.target

    # dataset 3
    """X_test = Xtest
    y_test = ytest"""

    #############################################################
    # Nettoyage des textes du dataset d'entraînement

    X_train = vectorisation_df(X_train)

    #############################################################
    # Nettoyage des textes du dataset de test

    X_test = vectorisation_df(X_test)

    #############################################################
    # Pipeline avec classifieur simple
    pipeline = Pipeline([('vectorizer', CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words(
        'english'))), ('tfidfconverter', TfidfTransformer()), ('classifier', RandomForestClassifier(n_estimators=1000, random_state=0))])

    # Pipeline avec classifieur simple sans TFIDF
    #pipeline = Pipeline([('vectorizer',CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))),('classifier',RandomForestClassifier(n_estimators=1000, random_state=0))])

    # Pipeline avec SVC
    #pipeline = Pipeline([('vectorizer',CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))),('tfidfconverter',TfidfTransformer()),('svc',SVC(C=100, kernel='sigmoid'))])

    # Pipeline avec SVC sans TFIDF
    #pipeline = Pipeline([('vectorizer',CountVectorizer(max_features = 1500,min_df=5, max_df=0.7, stop_words=stopwords.words('english'))),('svc',SVC(C=10, kernel='linear'))])

    # Création du modèle, entraînement et prédiction
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    # Evaluation du modèle
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

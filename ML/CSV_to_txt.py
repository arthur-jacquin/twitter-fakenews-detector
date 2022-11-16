import pandas as pd

#Extraction des données texte des fichiers csv
fake = pd.read_csv('../Dataset_Fake_News_eng/2e_set_avec_4_colonne/Fake.csv')
fk = list(fake['text'])
fk_label = [0]*len(fk)
legit = pd.read_csv('../Dataset_Fake_News_eng/2e_set_avec_4_colonne/True.csv')
lg = list(legit['text'])
lg_label = [1]*len(lg)

#Création du dataset purement textuel
data2 = fk + lg
data2_label = fk_label + lg_label
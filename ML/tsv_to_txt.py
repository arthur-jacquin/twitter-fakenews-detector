import pandas as pd

#Traitement dataset d'entraînement
data_train = pd.read_csv('../liar_dataset/train.tsv',sep='\t',names=['ID','label','statement','subject','speaker','speaker_job','state_info','party_affiliation','barely_true_count','false_count','half_true_count','mostly_true_count','pants_on_fire_counts','context'])
Xtrain = data_train['statement']
ytrainraw = data_train['label']

#Traitement dataset de test
data_test = data = pd.read_csv('../liar_dataset/test.tsv',sep='\t',names=['ID','label','statement','subject','speaker','speaker_job','state_info','party_affiliation','barely_true_count','false_count','half_true_count','mostly_true_count','pants_on_fire_counts','context'])
Xtest= data_test['statement']
ytestraw = data_test['label']


#Abaissement du nombre de classes

ytrain = []
ytest = []

for i in range(len(ytrainraw)):
    if ytrainraw[i] in ['barely_true','false','half-true']:
        ytrain.append('false')
    else:
        ytrain.append('true')

for i in range(len(ytestraw)):
    if ytestraw[i] in ['barely_true','false','half-true']:
        ytest.append('false')
    else:
        ytest.append('true')
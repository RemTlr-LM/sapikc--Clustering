import numpy as np
import pandas as pd
from mca import MCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets, linear_model
#% matplotlib inline

chemin='C:/Users/10160468/Documents/Projet/3 - Etude Pro/Modelisation/'

#dataset = np.loadtxt('C:/Users/10160468/Documents/Projet/3 - Etude Pro/Modelisation/Etude Pro - Data pour Modelisation2.csv', delimiter=";")
#with open(chemin + 'Etude Pro - Data pour Modelisation2.csv', 'r', encoding='utf-8', errors='ignore') as infile:
#    with open(chemin + '/Etude Pro - Data pour Modelisation2_UTF8.csv', 'w') as outfile:
#        outfile.write(infile.read())

# conversion du CSV en DF
CSV = pd.read_csv(chemin + 'Etude Pro - Data pour Modelisation2_UTF8.csv', sep=';')
# affichage du DF dans la console : taper le nom du DF dans la console ou print(NOM_DU_DF)
# Attention la 1ere ligne en python à le no : 0
#print(CSV[:3])  # les 3 premieres lignes

#print(CSV.describe())
dfForMCA = CSV.iloc[:, 1:6]
#print(dfForMCA[:3])
print(dfForMCA.describe())

#mcaFic=MCA(CSV,benzecri=False)
# Valeurs singulières
#print(mcaFic.L)


#lancement de la classification
#model = KMeans(3).fit(CSV)
#print(model.cluster_centers_)
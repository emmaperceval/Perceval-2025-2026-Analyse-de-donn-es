#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv", "r") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
print(pd.DataFrame(contenu))
# Question 6
print("le nombre de lignes est ", len(contenu))
print("le nombre de colonnes est ", len(contenu.columns))
# Question 7

ligne = pd.DataFrame(contenu).iloc[0]
liste_types = []
for element in ligne:
    liste_types.append(type(element))

print(liste_types)
# Question 8
print(contenu.head(0))
# Question 9
print(pd.DataFrame(contenu, columns=["Inscrits"]))
print(pd.DataFrame(contenu, columns=["Inscrits"]).sum())
# Question 10       

nb_total = []
for element in contenu.columns:
    if type(contenu[element][0]) != str:
        nb_total.append(pd.DataFrame(contenu, columns=[element]).sum())

print(nb_total)

# Question 11
os.makedirs('images.barres', exist_ok=True)

df = pd.read_csv("fichier.csv")

for idx in contenu.iterrows():
    departement = row["Libellé du département"]
    inscrits = row["Inscrits"]
    votants = row["votants"]
    
    plt.figure(figsize=(6,4))
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=["yellow", "red"])
    plt.title(f"Nombre d'inscrits et de votants - {departement}")
    
    
    filename = f"img_barres/{departement.replace('/', '-')}_inscrits_votants.png"
    plt.savefig(filename, dpi=150)
    plt.close()
    plt.show()


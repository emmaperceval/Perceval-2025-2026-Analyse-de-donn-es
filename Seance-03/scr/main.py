#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023import pandas as pd

import os

if not os.path.exists("img"):
    os.mkdir("img")

#fichier élection 

with open("data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8") as f:
    df = pd.read_csv(f)

# Sélection des colonnes quantitatives
quant = df.select_dtypes(include=[np.number])

#paramètres statistiques 

moyenne = round(quant.mean(), 2)
mediane = round(quant.median(), 2)
mode = round(quant.mode().iloc[0], 2)
ecart_type = round(quant.std(), 2)
ecart_abs = round((quant - quant.mean()).abs().mean(), 2)
etendue = round(quant.max() - quant.min(), 2)

# Regroupement des résultats
stats = pd.DataFrame({
    "Moyenne": moyenne,
    "Médiane": mediane,
    "Mode": mode,
    "Écart-type": ecart_type,
    "Écart absolu moyen": ecart_abs,
    "Étendue": etendue
})

print("\nPARAMETRES STATISTIQUES\n")
print(stats)

#quantiles

iqr = round(quant.quantile(0.75) - quant.quantile(0.25), 2)
idr = round(quant.quantile(0.9) - quant.quantile(0.1), 2)

print("\nDistance interquartile\n", iqr)
print("\nDistance interdécile\n", idr)

#la boite à moustache
for col in quant.columns:
    plt.figure()
    plt.boxplot(quant[col].dropna())
    plt.title(col)
    plt.savefig(f"img/boxplot_{col}.png")
    plt.close()

#fichier island 
with open("data/island-index.csv", encoding="utf-8") as f:
    island = pd.read_csv(f)

surface = island["Surface (km2)"]

# Classes de surface
bins = [0, 10, 25, 50, 100, 2500, 5000, 10000, np.inf]
labels = [
    "]0,10]", "]10,25]", "]25,50]", "]50,100]",
    "]100,2500]", "]2500,5000]", "]5000,10000]", "]10000,+∞["
]

classes = pd.cut(surface, bins=bins, labels=labels)

denombrer = classes.value_counts().sort_index()

print("\nNOMBRE D'ILES PAR CLASSE DE SURFACE\n")
print(denombrer)

stats.to_csv("statistiques_elections.csv")
stats.to_excel("statistiques_elections.xlsx")

print('Bienvenue dans le cours d\'analyse de données en géographie !')
import os
import pandas as pd
import numpy
import geopandas as gdp

from math import sqrt
from scipy.stats import shapiro

data = pd.DataFrame({'A': [1, 2, 3]})
print(data)


# Chargement des 100 échantillons
df = pd.read_csv("data/Echantillonnage-100-Echantillons.csv")

# Moyenne par opinion
moyennes = df.mean()
moyennes_arrondies = round(moyennes, 0)

print("Moyennes arrondies par opinion :")
print(moyennes_arrondies)

#  Fréquences issues des échantillons 
total_moyennes = moyennes_arrondies.sum()
frequences_echantillon = round(moyennes_arrondies / total_moyennes, 2)

print("\nFréquences (échantillons) :")
print(frequences_echantillon)

#  Fréquences de la population mère 
population = {
    "Pour": 852,
    "Contre": 911,
    "Sans opinion": 422
}

pop_series = pd.Series(population)
frequences_population = round(pop_series / pop_series.sum(), 2)

print("\nFréquences (population mère) :")
print(frequences_population)

#  Intervalles de fluctuation à 95 % 
z = 1.96
n = total_moyennes

intervalle_fluctuation = {}

for opinion, f in frequences_echantillon.items():
    marge = z * sqrt((f * (1 - f)) / n)
    intervalle_fluctuation[opinion] = (
        round(f - marge, 3),
        round(f + marge, 3)
    )

print("\nIntervalles de fluctuation (95 %) :")
for k, v in intervalle_fluctuation.items():
    print(f"{k} : {v}")


#  Sélection du premier échantillon 
echantillon_1 = list(df.iloc[0])

n1 = sum(echantillon_1)

# Fréquences de l’échantillon 
frequences_1 = [x / n1 for x in echantillon_1]

# Intervalles de confiance 
intervalle_confiance = []

for f in frequences_1:
    marge = z * sqrt((f * (1 - f)) / n1)
    intervalle_confiance.append(
        (round(f - marge, 3), round(f + marge, 3))
    )

print("\nIntervalles de confiance (échantillon 1) :")
for opinion, ic in zip(df.columns, intervalle_confiance):
    print(f"{opinion} : {ic}")


# Chargement des données
loi_1 = pd.read_csv("/Users/utilisateur/Desktop/MasterSorbonne/Perceval-2025-2026-Analyse-de-données/Seance-05/data/Loi-normale-Test-1.csv")
loi_2 = pd.read_csv("/Users/utilisateur/Desktop/MasterSorbonne/Perceval-2025-2026-Analyse-de-données/Seance-05/data/Loi-normale-Test-2.csv")

# Conversion en séries
valeurs_1 = loi_1.iloc[:, 0]
valeurs_2 = loi_2.iloc[:, 0]

# Test de Shapiro-Wilk
stat_1, p_1 = shapiro(valeurs_1)
stat_2, p_2 = shapiro(valeurs_2)

print("\nTest de Shapiro-Wilk :")
print(f"Loi 1 → statistique = {round(stat_1,4)}, p-value = {round(p_1,4)}")
print(f"Loi 2 → statistique = {round(stat_2,4)}, p-value = {round(p_2,4)}")


alpha = 0.05

print("\nInterprétation :")

if p_1 > alpha:
    print("Loi 1 : distribution compatible avec une loi normale")
else:
    print("Loi 1 : distribution non normale")

if p_2 > alpha:
    print("Loi 2 : distribution compatible avec une loi normale")
else:
    print("Loi 2 : distribution non normale")

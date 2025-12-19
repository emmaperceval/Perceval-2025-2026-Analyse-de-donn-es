#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Les fonctions générales:

def afficher_distribution_discrete(x, pmf, titre):
    plt.figure()
    plt.stem(x, pmf)
    plt.xlabel("Valeurs")
    plt.ylabel("Probabilité")
    plt.title(titre)
    plt.grid(True)
    plt.show()


def afficher_distribution_continue(x, pdf, titre):
    plt.figure()
    plt.plot(x, pdf)
    plt.xlabel("Valeurs")
    plt.ylabel("Densité")
    plt.title(titre)
    plt.grid(True)
    plt.show()


def moyenne_et_ecart_type(x, p):
    """
    x : valeurs
    p : probabilités ou densités (normalisées)
    """
    moyenne = np.sum(x * p)
    variance = np.sum((x - moyenne) ** 2 * p)
    return moyenne, np.sqrt(variance)


#Les distributions discrètes: 

# Loi de Dirac
x = np.arange(-5, 6)
p = stats.rv_discrete(values=(x, (x == 0).astype(int))).pmf(x)
afficher_distribution_discrete(x, p, "Loi de Dirac")
print("Dirac :", moyenne_et_ecart_type(x, p))

# Loi uniforme discrète
x = np.arange(1, 11)
p = stats.randint(1, 11).pmf(x)
afficher_distribution_discrete(x, p, "Loi uniforme discrète")
print("Uniforme discrète :", moyenne_et_ecart_type(x, p))

# Loi binomiale
n, p_bin = 20, 0.4
x = np.arange(0, n + 1)
p = stats.binom(n, p_bin).pmf(x)
afficher_distribution_discrete(x, p, "Loi binomiale")
print("Binomiale :", moyenne_et_ecart_type(x, p))

# Loi de Poisson (discrète)
lambda_poisson = 4
x = np.arange(0, 15)
p = stats.poisson(lambda_poisson).pmf(x)
afficher_distribution_discrete(x, p, "Loi de Poisson (discrète)")
print("Poisson discrète :", moyenne_et_ecart_type(x, p))

# Loi de Zipf-Mandelbrot
N = 20
s = 2
q = 1
x = np.arange(1, N + 1)
p = 1 / (x + q) ** s
p = p / p.sum()  # normalisation
afficher_distribution_discrete(x, p, "Loi de Zipf-Mandelbrot")
print("Zipf-Mandelbrot :", moyenne_et_ecart_type(x, p))

#Les distributions continues: 

# Loi normale
x = np.linspace(-4, 4, 400)
pdf = stats.norm(0, 1).pdf(x)
afficher_distribution_continue(x, pdf, "Loi normale")

# Loi log-normale
x = np.linspace(0.001, 5, 400)
pdf = stats.lognorm(s=0.5).pdf(x)
afficher_distribution_continue(x, pdf, "Loi log-normale")

# Loi uniforme continue
x = np.linspace(0, 10, 400)
pdf = stats.uniform(0, 10).pdf(x)
afficher_distribution_continue(x, pdf, "Loi uniforme continue")

# Loi du χ-2
x = np.linspace(0, 15, 400)
pdf = stats.chi2(df=4).pdf(x)
afficher_distribution_continue(x, pdf, "Loi du χ²")

# Loi de Pareto
x = np.linspace(1, 10, 400)
pdf = stats.pareto(b=2).pdf(x)
afficher_distribution_continue(x, pdf, "Loi de Pareto")

print("Manipulations terminées")
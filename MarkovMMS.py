#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:18:49 2020

@author: aymen
"""

import math

# initilaisation des parametres utilises dans les formules de little 
Ns = 0
Nf = 0
Ts = 0
Tf = 0
s = 0
Lambda = 0
Mu = 0
Ro = 0

# obtention du parametre a calculer
print("Veuillez donner le nombre de serveurs s = ")
s = int(input())
print("Veuillez donner le taux d'arrivee des clients Lambda = ")
Lambda = float(input())
print("Veuillez donner le duree de service Mu = ")
Mu = float(input())
print("Que voulez vous calculez ?")
print("1/ Nombre moyen des clients dans le systeme")
print("2/ Nombre moyen des clients dans la file")
print("3/ Temps d'attente moyen dans le systeme")
print("4/ Temps d'attente moyen dans la file")
parametre = int(input())
Ro = Lambda / (s * Mu)
u = Lambda / Mu

# definition des fonction de calcul des proba
def P0():
    somme = 0
    for i in range (0, s):
        somme = somme + ((u ** i) / math.factorial(i)) 
    temp = somme + (((u ** s) * s) / (math.factorial(s) * (s - u))) 
    return 1 / temp

def P(k):
    if(1 <= k) and (k <= s):
        return ((Lambda**k) / (math.factorial(k) * (Mu**k))) * P0()
    elif(k >= s):
        return ((Lambda**k) / (math.factorial(s) * (Mu**k) * (s**(k-s)))) * P0()

# calcul des parametres
if(Ro >= 1):
    print("ERREUR : Regime stationnaire n'existe pas !")
else:
    if parametre == 1:
        print("Calcul du nombre moyen des clients dans le systeme...")
        Ns = (Ro * P(s))/((1 - Ro)**2) + s * Ro
        print(Ns)
    elif parametre == 2:
        print("Calcul du nombre moyen des clients dans la file...")
        Nf = (Ro * P(s))/((1 - Ro)**2)
        print(Nf)
    elif parametre == 3:
        print("Calcul du temps d'attente moyen dans le systeme...")
        Ns = (Ro * P(s))/((1 - Ro)**2) + s * Ro
        Ts = Ns / Lambda
        print(Ts)
    elif parametre == 4:
        print("Calcul du temps d'attente moyen dans la file...")
        Nf = (Ro * P(s))/((1 - Ro)**2)
        Tf = Nf / Lambda
        print(Tf)
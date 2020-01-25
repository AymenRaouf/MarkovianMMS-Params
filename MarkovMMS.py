#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:18:49 2020

@author: aymen
"""

# initilaisation des parametres utilises dans les formules de little 
Ns = 0
Nf = 0
Ts = 0
Tf = 0

# obtention du parametre a calculer
print("Que voulez vous calculez ?")
print("1/ Nombre moyen de clients dans le systeme")
print("2/ Nombre moyen de clients dans la file")
print("3/ Temps d'attente moyen dans le systeme")
print("4/ Temps d'attente moyen dans la file")
parametre = int(input())

# calcul 
if parametre == 1:
    print("Calcul du nombre moyen des clients dans le systeme...")
if parametre == 2:
    print("Calcul du nombre moyen de clients dans la file...")
if parametre == 3:
    print("Calcul du temps d'attente moyen dans le systeme...")
if parametre == 4:
    print("Calcul du temps d'attente moyen dans la file...")
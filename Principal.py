# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:18:33 2020

@author: Estefany
"""

from Grafo import Grafo
import re

G = Grafo("Grafo")

archivo = open("kruskal.txt")
lineas = archivo.readlines()

for linea in lineas:
    a = re.findall("\S+", linea)
    
    if(len(a) > 2):
        G.addNodo(a[0])
        G.addNodo(a[1])
        G.getNodo(a[0]).addAdyacente(G.getNodo(a[1]))
        G.addArco(a[0], a[1], a[2])

G.MSTKRUSKAL()
G.showKRUSKAL()
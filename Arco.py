# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:41:32 2020

@author: Estefany
"""
from Nodo import Nodo

class Arco:
    def __init__(self, origen, destino, costo):
        self.origen = origen
        self.destino = destino
        self.costo = costo
    
    def add(self, origen, destino, costo):
        self.origen = Nodo(origen)
        self.destino = Nodo(destino)
        self.costo = costo
    
    def show(self):
        print(self.origen, self.destino, int(self.costo), sep = " ")
        
        
    
        
        
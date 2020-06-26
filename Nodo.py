# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:12:22 2020

@author: Estefany
"""


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adjunta = []
        self.d = 0
        self.f = 0
        self.padre = None
        self.rank = 0
        self.color = "Blanco"
        
    def show(self):
        if self.padre == None:
            p = " "
        else:
            p = self.padre.nombre
        print(self.nombre, " (", self.d, "/", self.f, ") raiz = ", p, " ",sep = "",end = " ")
        for i in self.adjunta:
            print(i.nombre, end = " ")
        print(" ")
        
    def addAdyacente(self, nodo):
        self.adjunta.append(nodo)
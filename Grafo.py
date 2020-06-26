# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:34:24 2020

@author: Estefany
"""

from Nodo import Nodo
from Arco import Arco

class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.V = {}
        self.E = []
    
    def addNodo(self, nodo):
        if nodo not in self.V:
            self.V[nodo] = Nodo(nodo)
            
    def getNodo(self, nodo):
        if nodo not in self.V:
            return None
        return self.V[nodo]
    
    def addArco(self, origen, destino, costo):
        self.E.append(Arco(origen, destino, float(costo)))
        
    def show(self):
        print("GRAFO: ")
        for i in self.V.values():
            i.show()   
        print("\nARCO: ")
        for i in self.E:
            i.show() 
          
            
    #DFS
    def DFS(self):
        for nodo in self.V.values():
            nodo.color = "Blanco"
            nodo.padre = None
        self.tiempo = 0
        
        for u in self.V.values():
            if u.color == "Blanco":
                self.DFS_Visit(u)
        
    def DFS_Visit(self, u):
        u.color = "Gris"
        self.tiempo = self.tiempo + 1
        u.d = self.tiempo
        for v in u.adjunta:
            if v.color == "Blanco":
                v.padre = u
                self.DFS_Visit(v)
        u.color = "Negro"
        self.tiempo = self.tiempo + 1
        u.f = self.tiempo
    
    def get_transpuesta(self):     
        G = Grafo("Grafo")
        
        for a in self.E:
            G.addNodo(a.destino)
            G.addNodo(a.origen)
            G.getNodo(a.destino).addAdyacente(G.getNodo(a.origen))
            G.addArco(a.destino, a.origen, a.costo)
            
        return G
    
    
    #KRUSKAL
    MST = []
    
    def MSTKRUSKAL(self):
        for v in self.V.values():
            self.make_set(v)
            
        self.E.sort(key=lambda x: x.costo)
        
        for arco in self.E:
            if self.find(arco.origen) != self.find(arco.destino):
                self.union(arco.origen, arco.destino)
                self.MST.append(arco)

    def make_set(self, nodo):
        nodo.padre = nodo
        
    def find(self, nodo):
        nodo = self.getNodo(nodo)
        padre = nodo.padre
        if padre == nodo:
            return nodo
        return self.find(padre.nombre)
    
    def union(self, origen, destino):
        u = self.find(origen)
        v = self.find(destino)
        
        if u != v:
            if u.rank < v.rank:
                u.padre = v
            else:
                v.padre = u
            if u.rank == v.rank:
                u.rank += 1
    
    def showKRUSKAL(self):
        print("\nMSTKRUSKAL: ")
        for i in self.MST:
            i.show()
        
        print("\nGRAFO: ")
        for i in self.V.values():
            i.show()   
    
    
    
    
    
    
    
    
    
    
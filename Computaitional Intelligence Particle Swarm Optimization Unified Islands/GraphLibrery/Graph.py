# -*- coding: utf-8 -*-
import numpy as np
from .Edge import Edge
class Graph(object) :
      
    def __init__(self):
        self.vertices = []
        self.edges = []
        
        
        
    def addVertex(self,vertex): 
        if vertex in self.vertices :
            print("Graph : addVertex : vertex is in the graph")
        self.vertices.append(vertex)
        """Mabye need copy"""
        
    def addEdge(self,first_vertex,second_vertex,wieght=0):
        if first_vertex not in self.vertices :
            print("Graph : addEdge : vertex is not the graph")
        if second_vertex not in self.vertices :
            print("Graph : addEdge : vertex is not the graph")
            
        newedge = Edge(first_vertex,second_vertex,wieght)
        self.edges.append(newedge) 
        """Mabye need copy"""
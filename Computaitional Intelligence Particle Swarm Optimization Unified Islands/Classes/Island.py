# -*- coding: utf-8 -*-
from .Particle import Particle
from .GraphLibrery import Graph
import numpy as np
class Island(object):
    
    def __init__(self,graph_func,island_size,particles,bounderies,acc_coeff_personal,acc_coeff_social,is_bounded = True,lb,ub)
        self.graph = graph_func(particles)
        self.size = island_size
        self.first_size = island_size
        self.boundery_conditions = bounderies
        self.acceleration_coeff_personal = acc_coeff_personal
        self.acceleration_coeff_social = acc_coeff_social
        self.is_bounded = is_bounded
        self.fitness_best_g = np.inf          
        self.position_best_g = np.empty([n])
        self.omega = 0.7298
        self.lb = lb
        self.ub = ub
        
    def UpdateIsland(self,objFunc=lambda x: x.dot(x)):
        for k in range(0,self.size):
           self.graph.vertices[k].evaluate(objFunc)
           if self.graph.vertices[k].fitness < self.fitness_best_g :
                    self.position_best_g = np.copy(self.graph.vertices[k].current_position)
                    self.fitness_best_g = self.graph.vertices[k].fitness
            
        for k in range(0,self.size):
            self.graph.vertices[k].update_velocity(self.position_best_g,self.acceleration_coeff_personal,self.acceleration_coeff_social,self.omega)
            self.graph.vertices[k].update_position(self.lb,ub)
            
        self.graph.updateEdgeWieght()
        """"
        
        TODO: enter the boid restrictions
        
        
        """"
        
        

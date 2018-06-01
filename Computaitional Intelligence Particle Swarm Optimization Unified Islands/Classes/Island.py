# -*- coding: utf-8 -*-
from .Particle import Particle

class Island(object):
    
    def __init__(self,graph_func,island_size,particles,bounderies,acc_coeff,is_bounded = True,leader):
        self.graph = graph_func(particles)
        self.size = island_size
        self.boundery_conditions = bounderies
        self.acceleration_coeff =acc_coeff
        self.is_bounded = is_bounded
        self.leader = leader
        
        
        

# -*- coding: utf-8 -*-
from .Particle import Particle
from GraphLibrery import Graph
import numpy as np
class Island(object):
    
    def __init__(self,island_size,acc_coeff_personal,acc_coeff_social,is_bounded,lb,ub,par_dim,global_optimum_value,op_num,bounderies=0):
        self.graph = []
        self.size = island_size
        self.first_size = island_size
        self.boundery_conditions = bounderies
        self.acceleration_coeff_personal = acc_coeff_personal
        self.acceleration_coeff_social = acc_coeff_social
        self.is_bounded = is_bounded
        self.fitness_best_g = np.inf          
        self.position_best_g = np.empty([par_dim])
        self.omega = 0.7298
        self.lb = lb
        self.ub = ub
        self.particle_dimention = par_dim
        self.local_state = np.random.RandomState()
        self.globalOptimaValue=global_optimum_value
        self.operationNumber = op_num
        self.flag=0
    
    def UpdateIsland(self,i,eps,objFunc=lambda x: x.dot(x)):
        for k in range(0,self.size):
           self.graph[k].evaluate(objFunc)
           if self.graph[k].fitness -eps <= self.globalOptimaValue and self.flag==0:
               string="GlobalOptForOperation"
               string2 = str(self.operationNumber)
               str3=string+string2+".txt"
               file=open(str3,"w")
               string = "Global Optimum Was found in iteration number " +str(i+k)
               file.write(string)
               self.flag=1
               file.close()
           if self.graph[k].fitness < self.fitness_best_g :
                    self.position_best_g = np.copy(self.graph[k].current_position)
                    self.fitness_best_g = self.graph[k].fitness
            
        for k in range(0,self.size):
            self.graph[k].update_velocity(self.position_best_g,self.acceleration_coeff_personal,self.acceleration_coeff_social,self.omega)
            self.graph[k].update_position(self.lb,self.ub)
            
        
    def InitializeParticlesRandomly(self): 
        particles = []
       
        for k in range (self.size):
            point = self.local_state.uniform(size=self.particle_dimention)*(self.ub - self.lb) + self.lb
            particles.append(Particle(point)) 
        self.graph= np.copy(particles) 
        

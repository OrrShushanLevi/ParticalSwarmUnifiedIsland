# -*- coding: utf-8 -*-
from .Island import Island
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Space(object):
    
    def __init__(self,objFunc,N,bound_enf_func_array,total_island_num,par_in_each_island_array,func_upp_b,func_low_b,graph_functions_array,acc_coeff_per_array,acc_coef_social_array,island_boundery_status_arr,island_particle_dim_arr,global_optimum_value,op_num,unified_flag = True):
        self.obj_func = objFunc
        self.n_iter = N
        self.boundery_enforcer = bound_enf_func_array
        self.total_islands = total_island_num
        self.particle_in_each_island = par_in_each_island_array
        self.obj_function_upper_bound = func_upp_b
        self.obj_function_lower_bound = func_low_b 
        self.unified_islands = unified_flag
        self.graph_function_array = graph_functions_array
        self.acc_coeff_per_array = acc_coeff_per_array
        self.acc_coeff_social_array = acc_coef_social_array
        self.island_array = []
        self.best_islands_leaders_position = [None] *total_island_num
        self.best_islands_leaders_fitness = [None] *total_island_num
        self.island_boundery_status_array = island_boundery_status_arr
        self.island_particle_dim_array = island_particle_dim_arr
        self.parplot = plt.subplot(111)
        self.globalOptimaValue=global_optimum_value
        self.epsilon = 0.0001
        self.operationNumber=op_num
        self.parfig = plt.figure()
        self.ax = self.parfig.add_subplot(111, projection="3d")
        
        step = 0.1
        self.grid_x = np.arange(func_low_b, func_upp_b+step, step)
        self.grid_y = np.arange(func_low_b, func_upp_b+step, step)
        self.grid_xx, self.grid_yy = np.meshgrid(self.grid_x, self.grid_y)
        self.obj_mesh=self.functionSurface(self.grid_x , self.grid_y , self.obj_func)

        
        
    def constructIslands(self):
        for k in range (self.total_islands):
            self.island_array.append(Island(self.particle_in_each_island[k],self.acc_coeff_per_array[k],self.acc_coeff_social_array[k],self.island_boundery_status_array[k],self.computeLowerBound(k),self.compueUpperBound(k),self.island_particle_dim_array[k],self.globalOptimaValue,self.operationNumber))
    def constructIslandsRandumlly(self):
        for k in range (self.total_islands):
            self.island_array.append(Island(self.particle_in_each_island[k],self.acc_coeff_per_array[k],self.acc_coeff_social_array[k],self.island_boundery_status_array[k],self.obj_function_lower_bound,self.obj_function_upper_bound,self.island_particle_dim_array[k],self.globalOptimaValue,self.operationNumber))
    
    def computeLowerBound(self,k):
        if k == 0 :
            return self.obj_function_lower_bound
        length = (self.obj_function_upper_bound - self.obj_function_lower_bound)/self.total_islands
        return self.obj_function_lower_bound + length*k
   
    def compueUpperBound(self,k):
        length = (self.obj_function_upper_bound - self.obj_function_lower_bound)/self.total_islands
        return (self.computeLowerBound(k)+length)
       
    def printAllParticleResault(self):
        for k in range (self.total_islands):
            for j in range (self.island_array[k].size):
                print("Particle number: ",j, " From Island number: ",k, " Best Score is: ",self.island_array[k].graph[j].fitness_pbest," In Position : ",self.island_array[k].graph[j].position_pbest)
    
    
    def functionSurface(self , x , y , f):
        m = np.zeros((np.size(x),np.size(y)))
        for i in range (np.size(x)):
            for j in range (np.size(y)):
                m[i][j] =f([x[i],y[j]])
        return m
    
        
    def plotParticlesIn3D(self):
        self.ax.clear()
        self.ax.set_xlim3d(self.obj_function_lower_bound , self.obj_function_upper_bound)
        self.ax.set_ylim3d(self.obj_function_lower_bound , self.obj_function_upper_bound)
        self.ax.set_zlim3d(self.obj_function_lower_bound , self.obj_function_upper_bound)
        #self.ax.plot_surface(self.grid_xx, self.grid_yy, self.obj_mesh, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
        

        
        
        for k in range (self.total_islands):
            if (k%7) ==0:
                color = 'b'
            if (k%7) ==1:
                color = 'g'
            if (k%7) ==2:
                color = 'r'
            if (k%7) ==3:
                color = 'c'
            if (k%7) ==4:
                color = 'm'
            if (k%7) ==5:
                color = 'y'
            if (k%7) ==6:
                color = 'b'
            
            
            for j in range (self.island_array[k].size):
                pos = self.island_array[k].graph[j].current_position
                self.ax.scatter(pos[0] , pos[1], pos[2],c = color , marker='+')        
        plt.show()
        plt.pause(0.2)
        
        
        
        
        
    def plotParticles(self):
        self.parplot.clear()
        self.parplot.contour(self.grid_xx, self.grid_yy, self.obj_mesh, 10, offset=-1, lw=3, colors="k", linestyles="solid", alpha=0.5)
        for k in range (self.total_islands):
            if (k%7) ==0:
                color = 'b'
            if (k%7) ==1:
                color = 'g'
            if (k%7) ==2:
                color = 'r'
            if (k%7) ==3:
                color = 'c'
            if (k%7) ==4:
                color = 'm'
            if (k%7) ==5:
                color = 'y'
            if (k%7) ==6:
                color = 'b'
            
            
            for j in range (self.island_array[k].size):
                pos = self.island_array[k].graph[j].current_position
                self.parplot.plot(pos[0] , pos[1],'+' + color)        
        plt.show()
        plt.pause(0.2)
        
        
    def printIslandLeadersResault(self):
        for k in range (self.total_islands):
             print("Island number: ", k," Best Score is: ",self.best_islands_leaders_fitness[k]," In Position : ",self.best_islands_leaders_position[k] )
            
            
            
            
    def printBound(self):
        for k in range (self.total_islands):
            print("Island number: ", k," is bound param is: ",self.island_array[k].is_bounded)
            
            
            
            
            
    def printToFile(self,file):
        for k in range (self.total_islands):
            for j in range (self.island_array[k].size):
                string = "Particle number: " + str(j) + " From Island number: " + str(k) + " Best Score is: " + str(self.island_array[k].graph[j].fitness_pbest) + " In Position : " + str(self.island_array[k].graph[j].position_pbest) + "\n"
                file.write(string)
        file.close()
        return
    
    
    
    
    
    def printAvgParticleScore(self):
        string="AvgParticleScoreForOperation"
        string2 = str(self.operationNumber)
        str3=string+string2+".txt"
        file=open(str3,"w")
        score_sum=0
        for k in range (self.total_islands):
            for j in range (self.island_array[k].size):
                score_sum+=self.island_array[k].graph[j].fitness_pbest
        string = "Score sum for operation " + str(self.operationNumber) + "is: " +str(score_sum) +"\n"
        file.write(string)
        file.close()
        return
    
    
    def standardIslandPSO(self):
        for k in range (self.total_islands):
            self.island_array[k].InitializeParticlesRandomly()
        i = 0 
        particlesum = 0
        for k in range (self.total_islands):
            particlesum+= self.island_array[k].size
        while i < self.n_iter:
                for k in range (self.total_islands):
                    self.island_array[k].UpdateIsland(i,self.epsilon,self.obj_func)
                    self.best_islands_leaders_position[k] = np.copy(self.island_array[k].position_best_g)
                    self.best_islands_leaders_fitness[k]= np.copy(self.island_array[k].fitness_best_g)
                   # print("Island k =",k," best score is : ",self.best_islands_leaders_fitness[k]," in position : ",self.best_islands_leaders_position[k])   
                i+= particlesum
                print("    iteration :  ",i)
               
                self.plotParticles()
     


             
    def ConvergingIslandsPSO(self):
        i = 0 
        particlesum = 0
        unificationparam=self.total_islands
        for k in range (self.total_islands):
            self.island_array[k].InitializeParticlesRandomly()
        
        for k in range (self.total_islands):
            particlesum+= self.island_array[k].size
        while i < self.n_iter:
                for k in range (self.total_islands):
                    self.island_array[k].UpdateIsland(i,self.epsilon,self.obj_func)
                    self.best_islands_leaders_position[k] = np.copy(self.island_array[k].position_best_g)
                    self.best_islands_leaders_fitness[k]= np.copy(self.island_array[k].fitness_best_g)
                i+= particlesum
                print("iteration number : ",i)
                #self.plotParticlesIn3D()
                self.plotParticles()
                if i>=np.rint(self.n_iter/unificationparam):
                    print("Unification is occuring!")
                    lowScoreIsland = 0 
                    highScoreIsland = 0
                    score =  self.best_islands_leaders_fitness[0]
                    for k in range (self.total_islands):
                        if score < self.best_islands_leaders_fitness[k] and self.island_array[k].is_bounded == 1:
                            score =  self.best_islands_leaders_fitness[k]
                            lowScoreIsland = k
                    score =  self.best_islands_leaders_fitness[0]
                    for k in range (self.total_islands):
                        if score > self.best_islands_leaders_fitness[k] and self.island_array[k].is_bounded == 1:
                            score =  self.best_islands_leaders_fitness[k]
                            highScoreIsland = k
                    self.island_array[lowScoreIsland].is_bounded = 0
                    self.island_array[lowScoreIsland].lb=self.obj_function_lower_bound
                    self.island_array[lowScoreIsland].ub=self.obj_function_upper_bound
                    self.island_array[lowScoreIsland].acceleration_coeff_personal=0
                    #self.island_array[lowScoreIsland].acceleration_coeff_social = 2*self.island_array[lowScoreIsland].acceleration_coeff_social
                    self.island_array[lowScoreIsland].position_best_g = np.copy(self.island_array[highScoreIsland].position_best_g)
                    self.island_array[lowScoreIsland].fitness_best_g = np.copy(self.island_array[highScoreIsland].fitness_best_g)
                    if unificationparam > 0 :
                        unificationparam = unificationparam - 1
                    
                    
                            
                    
                
                        
                    
             
                
            
        
        
        
        
      
        
        
        
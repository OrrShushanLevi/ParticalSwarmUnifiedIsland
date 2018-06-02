# -*- coding: utf-8 -*-
from .Island import Island
import numpy as np
class Space(object):
    
    def __init__(self,objFunc,N,bound_enf_func,island_num,par_num,func_upp_b,func_low_b,unified_flag = True,graph_functions,acc_coeff_per,acc_coef_social):
        self.obj_func = objFunc
        self.n_iter = N
        self.boundery_enforcer = bound_enf_func
        self.island_number = island_num
        self.particle_in_island = par_num
        self.function_upper_bound = func_upp_b
        self.function_lower_bound = func_low_b 
        self.unified_islands = unified_flag
        self.graph_function_array = graph_functions
        self.acc_coeff_per = acc_coeff_per
        self.acc_coef_social = acc_coef_social
        self.island_array = []
        self.best_islands_leaders = []
        
        
        def constructIslands(self):
            for k in range (self.island_number):
                self.island_array.append(Island(self.graph_function_array[k],self.particle_in_island[k],self.acc_coeff_per[k],self.acc_coeff_social[k],np.dot(k/self.island_number,function_lower_bound),np.dot(k/self.island_number,function_upper_bound)))
        
        
        
        
        
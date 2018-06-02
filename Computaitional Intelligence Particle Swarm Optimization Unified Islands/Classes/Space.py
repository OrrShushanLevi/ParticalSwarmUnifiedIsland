# -*- coding: utf-8 -*-
from .Island import Island
import numpy as np
class Space(object):
    
    def __init__(self,objFunc,N,bound_enf_func,island_num,par_num):
        self.obj_func = objFunc
        self.n_iter = N
        self.boundery_enforcer = bound_enf_func
        self.island_number = island_num
        self.particle_in_island=par_num

# -*- coding: utf-8 -*-
"""from .Space import Space"""
from BenchmarkFunctions import objFunctions
"""from Classes import Space"""
from Classes import Space
from Classes import Particle
from Classes import Island


"""def main():"""
   
    
    

if __name__ == "__main__":
    lb = 0.25
    ub = 10
    dim = 2
    objfunc = objFunctions.VincentFunction
    island = Island.Island(10,1.49,1.49,0,lb,ub,dim)
    island.InitializeParticlesRandomly()
    maxevals = 100000
    c = 0
    boundery_arr= [1]*36
    par_arr = [10]*36
    acc_coeff = [1.49]*36
    dim_arr= [2]*36
    space = Space.Space(objfunc,maxevals,boundery_arr,36,par_arr,ub,lb,par_arr,acc_coeff,acc_coeff,boundery_arr,dim_arr)
    space.constructIslands()
    space.standardIslandPSO()
        
   
        
    
    
    
    
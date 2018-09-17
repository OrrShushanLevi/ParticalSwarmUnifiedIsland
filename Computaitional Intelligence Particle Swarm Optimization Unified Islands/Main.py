# -*- coding: utf-8 -*-
"""from .Space import Space"""
from BenchmarkFunctions import objFunctions
import matplotlib.pyplot as plt
"""from Classes import Space"""
from Classes import Space
from Classes import Particle
from Classes import Island


"""def main():"""
   
    
    

if __name__ == "__main__":
    lb = objFunctions.GetVincentLB()
    ub = objFunctions.GetVincentUB()
    dim = 2
    numofparticles = 100
    numofislands = 10
    objfunc = objFunctions.VincentFunction
    maxevals = 3000*dim*dim
    boundery_arr= [1]*numofislands
    par_arr = [numofparticles]*numofislands
    acc_coeff = [1.49]*numofislands
    dim_arr= [dim]*numofislands
    space = Space.Space(objfunc,maxevals,boundery_arr,numofislands,par_arr,ub,lb,par_arr,acc_coeff,acc_coeff,boundery_arr,dim_arr)
    space.constructIslands()
    #space.standardIslandPSO()
    space.ConvergingIslandsPSO()
    space.printAllParticleResault()
    #space.printIslandLeadersResault()
    
 
        
   
        
    
    
    
    
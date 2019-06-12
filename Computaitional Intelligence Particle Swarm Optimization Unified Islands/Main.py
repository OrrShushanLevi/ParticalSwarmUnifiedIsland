# -*- coding: utf-8 -*-
from BenchmarkFunctions import objFunctions
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

from Classes import Space
from Classes import Particle
from Classes import Island




"""def main():"""
   
    

    

if __name__ == "__main__":
    objfunc = objFunctions.VincentFunction
    lb = objFunctions.GetVincentLB()
    ub = objFunctions.GetVincentUB()
    f = open("configForVincent2d.txt","r")
    dim = int(f.readline())
    numofislands = int(f.readline())
    numofparticles = int(f.readline())
    acc_coeff = float(f.readline())
    global_optima_val = float(f.readline())
    maxevals = 1000*dim*dim
    boundery_arr= [1]*numofislands
    par_arr = [numofparticles]*numofislands
    acc_coeff_array = [acc_coeff]*numofislands
    acc_coeff_zeors = [acc_coeff]*numofislands
    dim_arr= [dim]*numofislands
    operation_number=0
    max_oper=1
    while operation_number<max_oper:
        string = "OperationNumber"+str(operation_number)
        string2=".txt"
        bl=string+string2
        space = Space.Space(objfunc,maxevals,boundery_arr,numofislands,par_arr,ub,lb,par_arr,acc_coeff_array,acc_coeff_zeors,boundery_arr,dim_arr,global_optima_val,operation_number)
        #space.constructIslandsRandumlly()
        space.constructIslands()
        #space.standardIslandPSO()
        space.ConvergingIslandsPSO()
        file=open(bl,"w")
        space.printToFile(file)
        space.printAvgParticleScore()
        operation_number+=1

    
    
    
    #space.printAllParticleResault()
    #space.printIslandLeadersResault()
    #x = np.linspace(0.25, 10, 30)
    #y = np.linspace(0.25, 10, 30)
    #X, Y = np.meshgrid(x, y)
    #print(np.size(X))
    #z = objfunc(X)
    #Z = ([z]*2,[z]*30)
    #fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #ax.contour3D(X, X, Z, 50, cmap='binary')
    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    #ax.set_zlabel('z');
    
    
 
        
   
        
    
    
    
    
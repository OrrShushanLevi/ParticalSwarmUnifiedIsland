# -*- coding: utf-8 -*-
import numpy as np

def VincentFunction(x):
    return (1/np.size(x)*np.sum(np.sin(10*np.log(x))))
def GetVincentUB():
    return 10
def GetVincentLB():
    return 0.25
def ModifiedRastrigin(x):
    K=[4,5]
    Xk = np.multiply(x,K)
    return -(np.sum(10 +9*np.cos(2*np.pi*Xk)))
def GetModifiedRastriginUB():
    return 1
def GetModifiedRastriginLB():
    return 0



def rastrigin( x ):
    D = np.size(x)
    print(x)
    return -(10*( D - sum([ np.cos(2*np.pi*xi) for xi in x]) ) + np.dot(x,x)) 
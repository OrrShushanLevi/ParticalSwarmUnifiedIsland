# -*- coding: utf-8 -*-
import numpy as np

def VincentFunction(x):
    return (1/np.size(x)*np.sum(np.sin(10*np.log(x))))
def GetVincentUB():
    return 10
def GetVincentLB():
    return 0.25
def 


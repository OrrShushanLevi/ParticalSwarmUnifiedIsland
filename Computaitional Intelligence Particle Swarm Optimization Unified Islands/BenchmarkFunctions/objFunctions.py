# -*- coding: utf-8 -*-
import numpy as np

def VincentFunction(x):
    return (1/np.size(x)*np.sum(np.sin(10*np.log(x))))
def GetVincentUB():
    return 10
def GetVincentLB():
    return 0.25
def ModifiedRastrigin(x):
    return -(np.sum(10 +9*np.cos(2*np.pi*5*x)))
def GetModifiedRastriginUB():
    return 1
def GetModifiedRastriginLB():
    return 0
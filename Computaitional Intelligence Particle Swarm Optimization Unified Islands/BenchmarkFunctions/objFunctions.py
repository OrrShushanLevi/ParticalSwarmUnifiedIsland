# -*- coding: utf-8 -*-
import numpy as np
def VincentFunction(x):
    return (1/np.size(x)*np.sum(np.sin(10*np.log(x))))

"""
vincent is defiened for x in range 1/4 to 10
"""

# -*- coding: utf-8 -*-

import numpy as np



def tasy( beta : float, x : np.ndarray) -> np.ndarray:
    D = x.shape[0]
    p = lambda i, xi : 1 + beta * (i-1)/(D-1) * np.sqrt( xi )
    f = lambda i, xi : np.power(xi, p(i, xi)) if xi > 0 else xi
    return np.array( [ f(i,xi) for i, xi in enumerate(x) ], dtype=x.dtype )


def tosz( x ):
    c1 = lambda xi : 10 if xi > 0 else 5.5
    c2 = lambda xi : 7.9 if xi > 0 else 3.1
    tlog = lambda xi : np.log(np.abs(xi)) if xi != 0 else 0
    sign = lambda xi : -1 if xi < 0 else 1 if xi > 0 else 0
    sinsum = lambda xi : np.sin( c1(xi)*tlog(xi) ) + np.sin( c2(xi)*tlog(xi) )
    f = lambda xi : sign(xi) * np.exp( tlog(xi) + 0.049*( sinsum(xi) ) )
    return np.vectorize(f)(x)
    # return np.array( [ f(xi) for xi in x ], dtype=x.dtype )


def Lam( alpha, D ):
    return np.diag([ alpha**(0.5*(i-1)/(D-1)) for i in range(1, D+1) ])



# test1 = np.random.rand(10)
# print(test1)
# #test2 = tasy(test1, 0.9)
# test2 = tosz(test1)
# print(test2)
# import matplotlib.pyplot as plt
# plt.scatter(test1, test2)
# plt.show()
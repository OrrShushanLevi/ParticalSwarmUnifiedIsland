from BenchmarkFunctions import 

def rastrigin_scheme( x_opt, f_opt ):
    D = x_opt.shape[ 0 ]
    def rastrigin( x ):
        z = np.diag(Lam( 10, D )) * tasy( 0.2, tosz( x - x_opt ) )
        return 10*( D - sum([ np.cos(2*np.pi*zi) for zi in z ]) ) + np.dot(z,z) + f_opt
    return rastrigin



# import matplotlib.pyplot as plt
# from matplotlib import cm
#
# dx = 0.01
# X = np.arange(-5, 5, dx)
# Y = np.arange(-5, 5, dx)
# X, Y = np.meshgrid(X, Y)
# rastrigin = rastrigin_scheme( np.array([0,0]), 0 )
#
# Z = [ [ rastrigin(np.array([X[i,j],Y[i,j]])) for j in range(X.shape[1])] for i in range(X.shape[0]) ]
#
# #['Blues', 'Reds', 'hot', 'YlOrRd', 'seismic', 'Pastel2', 'YlOrBr', 'gist_ncar', 'winter', 'bwr', 'prism', 'RdYlBu', 'afmhot', 'BuGn', 'Accent', 'Paired', 'Oranges', 'RdBu', 'YlGn', 'CMRmap', 'PuBu', 'ocean', 'Purples', 'Pastel1', 'coolwarm', 'hsv', 'gist_rainbow', 'gist_heat', 'Greys', 'RdYlGn', 'gist_gray', 'flag', 'gist_stern', 'gnuplot', 'spring', 'pink', 'bone', 'PuOr', 'autumn', 'Spectral', 'brg', 'BrBG', 'OrRd', 'PuRd', 'gray', 'BuPu', 'nipy_spectral', 'gist_yarg', 'Dark2', 'jet', 'PRGn', 'terrain', 'PuBuGn', 'GnBu', 'RdGy', 'copper', 'spectral', 'gist_earth', 'summer', 'Set3', 'rainbow', 'Set1', 'PiYG', 'RdPu', 'cubehelix', 'Greens', 'YlGnBu', 'gnuplot2', 'cool', 'binary', 'Set2']
#
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# surf = ax.plot_surface(X, Y, np.array(Z), cmap=cm.summer,  linewidth=0, antialiased=True)
# plt.show()

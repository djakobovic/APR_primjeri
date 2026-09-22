# program_3_22.py
'''
   Crtanje plohe funkcije f(x_0,x_1)= sin(sqrt(x_0**2+x_1**2))
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext',fontset='stix')

x_0 = np.linspace(-5,5,201)
x_1 = np.linspace(-5,5,201)
X_0,X_1 = np.meshgrid(x_0,x_1)

def func(X_0,X_1):
    return np.sin(np.sqrt(X_0**2 + X_1**2))

F = func(X_0,X_1)

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X_0,X_1,F, cmap='seismic')
    ax.set_title(r'$f(x_0,x_1)=\sin\sqrt{x_0^2+x_1^2}$',fontsize=12)
    ax.set_xlabel(r'$x_0$',fontsize=12)
    ax.set_ylabel(r'$x_1$',fontsize=12)
    ax.set_zlabel(r'$f(x_0,x_1)$')
 
    fig.savefig('sl.3.24.pdf')
    fig.show()

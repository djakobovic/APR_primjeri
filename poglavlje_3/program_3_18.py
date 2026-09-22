# program_3_18.py
'''
Crtanje kontura funkcije z = x**2+y**2 - 2
mrežom od 201x201 tocaka
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext', fontset = 'stix')

x_0 = np.linspace(-2,2,201)
x_1 = np.linspace(-2,2,201)
X_0, X_1 = np.meshgrid(x_0,x_1)
F = X_0**2+X_1**2 - 2

fig,ax = plt.subplots()

if __name__ == '__main__':
    ax.set(aspect='equal',
           xlabel=r'$x_0$',ylabel=r'$x_1$',
           title=r'$f(x_0, x_1) = x_0^2 + x_1^2 - 2$')
    kont = ax.contour(X_0, X_1, F)
    ax.clabel(kont)
    ax.plot(0.0, 0.0, 'ko', ms = 4)
    ax.text(0.05, 0.05, r'$f(0,0)=-2$')

    fig.savefig('sl.3.20.pdf')
    fig.show()

# program_3_19.py
'''
Crtanje kontura funkcije f(x_0,x_1) = x_0**2+x_1**2 - 2 odabranim vrijednostima
razina i to:
  - u ax0 u jednoj boji s crtkanim negativnim konturama;
  - u ax1 uz negative_linestyles='-' i te su konture pune crte.   
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext',fontset='stix')

x_0 = np.linspace(-2,2,201)
x_1 = np.linspace(-2,2,201)
X_0,X_1 = np.meshgrid(x_0,x_1)
F = X_0**2+X_1**2 - 2
razine = np.array([-1.85, -1.5, -1, 0, 1, 2, 3])

fig,(ax0,ax1)=plt.subplots(1,2,layout='constrained')

if __name__ == '__main__':
    ax0.set(aspect='equal', xlabel=r'$x_0$',ylabel=r'$x_1$')
    ax0.set_title('Negativne konture crtkano',fontsize=10)
    ax0.axvline(c='gray',lw=1.0); ax0.axhline(c='gray',lw=1.0)    
    kontura0 = ax0.contour(X_0, X_1,F,levels=razine,colors='k',linewidths=0.8)
    ax0.clabel(kontura0,inline=True,fontsize=7)

    ax1.set(aspect='equal',xlabel=r'$x_0$',ylabel='$x_1$')
    ax1.set_title('Negativne konture punom crtom',fontsize=10)
    ax1.axvline(c='gray',lw=1.0); ax1.axhline(c='gray',lw=1.0)    
    kontura1 = ax1.contour(X_0,X_1,F,levels=razine,colors='k',linewidths=0.8,
                         negative_linestyles='-')
    ax1.clabel(kontura1,inline=True,fontsize=7)

    fig.savefig('sl.3.21.pdf')
    fig.show()

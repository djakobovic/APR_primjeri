# program_3_16.py
'''
Crtanje grafa funkcije y = 3+x/((x - 2)(x + 1)) u intervalu [-5,5]
s maskiranom funkcijom y u blizini polova uz crtanje
horizontalne i vertikalnih asimptota
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y= 3 + x/((x - 2)*(x +1))

fig,ax = plt.subplots(layout='constrained')

if __name__ == '__main__':
    ax.set(xlim=(-5,5),ylim=(0,5),xlabel='x',ylabel='y',
               title='y = 3 + x/((x-2)*(x+1))')
    ax.plot(x,np.ma.masked_outside(y,-30,30),'k-',lw=1.0)    
    ax.axvline(x=-1,c='k',ls='--',lw=1.0)
    ax.text(-3, 4.5, 'asimptota x=-1', c='k', fontsize=10)
    ax.axvline(x=2,c='k',ls='--',lw=1.0)
    ax.text(2.2, 0.5, 'asimptota x=2', c='k', fontsize=10)
    ax.axhline(y=3,c='k',ls='--',lw=1.0)    
    ax.text(-4.5, 3.2, 'asimptota y=3', c='k', fontsize=10)   

    fig.savefig('sl.3.18.pdf')
    fig.show()

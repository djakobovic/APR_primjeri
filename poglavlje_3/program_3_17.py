# program_3_17.py
'''
Funkcija tangens ima polove
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,101)
y = np.tan(x)

fig,ax = plt.subplots()

if __name__ == '__main__':
    ax.set(xlabel='x', ylabel='y',
           title='Funkcija tangens ima polove',
           xlim=(-2*np.pi,2*np.pi), ylim=(-5,5))
    ax.plot(x, np.ma.masked_outside(y,-10,10),c='k',lw=0.7)
    ax.axvline(c='b',lw=1.0); ax.axhline(c='b',lw=1.0)
    for i in range(4):
        ax.axvline(x=(1.5-i)*np.pi,c='k',ls='--',lw=0.7)

    fig.savefig('sl.3.19.pdf')
    fig.show()

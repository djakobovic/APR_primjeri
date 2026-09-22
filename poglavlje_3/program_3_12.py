# program_3_12.py
'''
Opis grafickog prikaza u stilu jezika LaTex
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext', fontset='stix')

x = np.linspace(0,5,201)
fig,ax = plt.subplots()    

if __name__ == '__main__':
    ax.set_title('Presjecanje funkcija: ' +r'$y=10x$'+', '
              +r'$y=3x^2$ '+'i '+r'$y=x^3$')
    ax.set(xlim=(2.5,3.5), ylim=(20.,40.), xlabel=r'$x$',
           ylabel=r'$f(x)$',xticks = np.arange(25,36)/10,
           yticks = np.arange(20,42,2))             
    ax.plot(x, 10 * x, 'r-', label=r'$10x$')
    ax.plot(x, 3 * x**2, 'b-.',label=r'$3x^2$')
    ax.plot(x, x**3, 'k:', label=r'$x^3$')                                  
    ax.legend(loc='upper left', title=r'$f(x)$')
    ax.grid(axis='both', c='gray', ls=':', lw=0.5)

    fig.savefig('sl.3.15.pdf')
    fig.show()

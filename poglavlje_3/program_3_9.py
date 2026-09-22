# program_3_9.py
'''
Crtanje koordinatnog sustava s koordinatnim osima,
parabolama i pravcima
'''
import matplotlib.pyplot as plt
import numpy as np

def koord_sust(naziv,x_granice,y_granice,x_tikovi,y_tikovi):
    ax.set(title=naziv,xlim=x_granice,ylim=y_granice,
           xticks=x_tikovi,yticks=y_tikovi)
    ax.grid(axis='both', color='gray',ls=':',lw=0.5)
    ax.axhline(color='grey',ls='-',lw=1.)
    ax.axvline(color='grey',ls='-',lw=1.)

if __name__ == '__main__':
    fig,ax = plt.subplots()
    x = np.linspace(-5,5,num=251)
    naziv = 'Koordinatne osi, parabole i pravci'
    x_gr = (-5,5); y_gr = (-5,5)
    x_t = np.arange(-5,6); y_t = np.arange(-5,6)
    koord_sust(naziv,x_gr,y_gr,x_t,y_t)
    ax.set(xlabel = 'x', ylabel = 'y')
    ax.plot(x,x,'b-',label='x')
    ax.plot(x,-x,'r-',label='-x')
    ax.plot(x,0.5*x**2,'k-',label='0.5*x**2')
    ax.plot(x,4-x**2,'g-',label='4-x**2')
    ax.legend(loc='best',title='y=f(x)')

    fig.savefig('sl.3.12.pdf')
    fig.show()

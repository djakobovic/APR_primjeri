# program_3_5.py
'''
Primjeri formatiranja prikaza funkcija
markerima i krivuljama
'''
import numpy as np
import matplotlib.pyplot as plt

xm = np.arange(6)                           
x = np.linspace(0,5,201)

if __name__ == '__main__':
    fig, ((ax0,ax1),(ax2,ax3)) = plt.subplots(2, 2, layout='constrained')
    '''crtež axs0'''
    ax0.set(xlabel='x', ylabel ='f(x)',
            title='Crtanje markera')
    ax0.plot(xm, 10 * xm, 'ro', label='10*x',ms=4)  
    ax0.plot(xm, 3 * xm**2, 'bv',label='3*x**2', ms=4)    
    ax0.plot(xm, xm**3, 'ks', label='x**3', ms=4)
    ax0.legend(loc='upper left', title='f(x)')
    '''crtež axs1'''
    ax1.set(xlabel='x', ylabel='f(x)',
            title='Crtanje markera sa spojnicama')
    ax1.plot(xm, 10 * xm, 'ro-', label='10*x', ms=4)
    ax1.plot(xm, 3 * xm**2, 'bv-.',label='3*x**2', ms=4)
    ax1.plot(xm, xm**3, 'ks:', label='x**3', ms=4)
    ax1.legend(loc='upper left', title='f(x)')
    '''crtež axs2'''
    ax2.set(xlabel='x', ylabel='f(x)',
            title='Crtanje glatkih krivulja')
    ax2.plot(x, 10 * x, 'r-', label='10*x')
    ax2.plot(x, 3 * x**2, 'b-.',label='3*x**2')
    ax2.plot(x, x**3, 'k:', label='x**3')
    ax2.legend(loc='upper left', title='f(x)') 
    '''crtež axs3'''
    ax3.set(xlabel='x', ylabel='f(x)',
            title='Glatke krivulje s markerima')
    ax3.plot(x, 10 * x, 'r-', label='10*x') 
    ax3.plot(x, 3 * x**2, 'b-.',label='3*x**2')
    ax3.plot(x, x**3, 'k:', label='x**3')
    ax3.legend(loc='upper left', title='f(x)')
    ax3.plot(xm, 10 * xm, 'ro', ms=4)      
    ax3.plot(xm, 3 * xm**2, 'bv', ms=4)
    ax3.plot(xm, xm**3, 'ks',ms=4)

    fig.savefig('sl.3.8.pdf')
    fig.show()




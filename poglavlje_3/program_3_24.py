# program_3_24.py
'''
Funkcija tangens uz oznake na osima
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-7,7,101)
y = np.tan(x)
plt.rc('mathtext', fontset='stix')

x_gr = (-7,7)
y_gr = (-5.5,5.5)

fig,ax = plt.subplots()

if __name__ == '__main__':
    ax.set(title=r'$Funkcija$ $tangens$ $ima$ $polove$',
           xlim=x_gr, ylim=y_gr)
    '''
    Vrijednostu np.tan(x) se maskiraju tako da se izbjegne eventualno
    spajanje pozitivnih i negativnih vrijednoti u blizini asimptota.
    '''
    ax.plot(x, np.ma.masked_outside(y,-15,15),c='k',lw=0.7)
    '''
    Crtanje asimptota.
    '''
    for i in range(4):
        ax.axvline(x=(1.5-i)*np.pi,c='k',ls='--',lw=0.7)
    '''
    Crtanje koordinata.
    '''
    ax.spines[['left', 'bottom']].set_position('center')
    ax.set_xticks([-6,-4,-2,2,4,6],[r'$-6$',r'$-4$',r'$-2$',r'$2$',r'$4$',r'$6$'])
    ax.set_yticks([-4,-2,2,4,],[r'$-4$',r'$-2$',r'$2$',r'$4$'])
    ax.spines[['top', 'right']].set_visible(False)
    ax.text(6.9,-0.08,r'$x$',ha='center',va='top')
    ax.text(0.3,5.4,r'$y$',ha='left',va='center')
    '''
    Crtanje strelica na x i y osi.
    '''
    ax.plot(x_gr[1]-0.12,0.,'k>',ms=5)
    ax.plot(0.,y_gr[1]-0.12,'k^',ms=5)

    fig.savefig('sl.3.26.pdf')
    fig.show()

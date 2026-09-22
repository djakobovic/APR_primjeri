# program_3_11.py.
'''
Program je svojevrsna tablica iz koje se moze sagledati nacine
pisanja pojedinih simbola, operacija i prikaza u jeziku mathtext
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext', fontset='stix')

fig,ax = plt.subplots()

if __name__ == '__main__':
    ax.set(title='Pisanje matematickih simbola i izraza u stilu jezika LaTeX',
           xlim=(0,10), ylim=(0,10))
    '''
    Mala grcka slova
    '''
    ax.text(0.5, 9, 'Mala grcka slova')
    ax.text(1, 8.5, r'$\alpha$'); ax.text(2, 8.5, r'$\beta$')
    ax.text(3, 8.5, r'$\gamma$'); ax.text(4, 8.5, r'$\delta$')
    ax.text(5, 8.5, r'$\varphi$'); ax.text(6, 8.5, r'$\omega$')
    ax.text(7, 8.5, r'$\pi$')
    '''
    Velika grcka slova
    '''
    ax.text(0.5, 8, 'Velika grcka slova')
    ax.text(1, 7.5, r'$\Delta$'); ax.text(2, 7.5, r'$\Sigma$')
    ax.text(3, 7.5, r'$\Gamma$'); ax.text(4, 7.5, r'$\Delta$')
    ax.text(5, 7.5, r'$\Phi$'); ax.text(6, 7.5, r'$\Omega$')
    ax.text(7, 7.5, r'$\Pi$')
    '''
    Trigonometrijske funkcije
    '''
    ax.text(0.5, 6.5, 'Trigonometrijske funkcije')
    ax.text(1, 6, r'$y = \sin(x)$'); ax.text(3, 6, r'$y = \cos(x)$')
    ax.text(5, 6, r'$y = \tan(x)$'); ax.text(1, 5.5, r'$y = \arcsin(x)$')
    ax.text(3, 5.5, r'$y = \arccos(x)$'); ax.text(5, 5.5, r'$y = \arctan(x)$')
    '''
    Pisanje potencija i indeksa
    '''
    ax.text(0.5, 4.5, 'Pisanje potencija i indeksa')
    ax.text(1, 4, r'$x^a$'); ax.text(2, 4, r'$x_i$')
    ax.text(3, 4, r'$\alpha_i > \beta_j^2$')
    '''
    Korjenovanje
    '''
    ax.text(0.5, 3, 'Korjenovanje')
    ax.text(1, 2.5, '$\sqrt{2}$'); ax.text(3, 2.5, r'$c = \sqrt{a^2 + b^2}$')
    '''
    Razlomci
    '''
    ax.text(0.5, 1.5, 'Razlomci')
    ax.text(1, 0.8, r'$\frac{3}{x}$', fontsize=12);
    ax.text(3, 0.8, r'$\frac{3}{x}$', fontsize=14)
    ax.text(5, 0.8, r'$\frac{1}{x} + \frac{1}{1 + \frac{1}{x}}$', fontsize=14)

    fig.savefig('sl.3.14.pdf') 
    fig.show()                                       

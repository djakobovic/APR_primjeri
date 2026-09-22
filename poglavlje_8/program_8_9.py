# program_8_9.py
'''
Algoritam Hooke-Jeeves
'''
import matplotlib.pyplot as plt
import program_8_6 as f2d

def hooke_jeeves(f, x0 = [0,0], maxiter = 99, eps = 0.000001, delta = [1,1], ax = None, korak = 0):
    '''
    f: funkcija cilja
    x0: pocetna tocka
    maxiter: najveci broj iteracija
    eps: preciznost
    ax: objekt subplot za prikaz
    delta: vektor pocetnih pomaka
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    xb = x0
    xp = xb.copy()
    for i in range (maxiter):
        fb = f(xb)
    
        # pretrazivanje
        xn = xp.copy()
        for dim in range (2):
            fp = f(xn)
            xn[dim] += delta[dim]
            fn = f(xn)
            if fn > fp:
                xn[dim] -= 2 * delta[dim]
                fn = f(xn)
                if fn > fp:
                    xn[dim] += delta[dim]

        if ax and (korak == 0 or korak == i):
            ax.scatter(xb[0], xb[1], c='r')
            ax.scatter(xp[0], xp[1], c='b')
            ax.scatter(xn[0], xn[1], c='k')
            if fn < fb:
                ax.plot([xb[0], 2*xn[0]-xb[0]], [xb[1], 2*xn[1]-xb[1]], c='k', lw=1, ls='--')

        # provjera napretka
        if fn < fb:
            for dim in range (2) :
                xp[dim] = 2 * xn[dim] - xb[dim]
            xb = xn.copy()
        else:
            for dim in range (2) :
                delta[dim] /= 2
            xp = xb.copy()

        if delta[0] < eps:
            break

    return xb

if __name__ == '__main__':
    # odabir funkcije cilja 
    f = f2d.booth; konture = f2d.booth_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture)
    # parametri postupka
    delta = [1, 1]
    x = hooke_jeeves(f, [1.3, 0.1], delta = delta, ax = ax)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
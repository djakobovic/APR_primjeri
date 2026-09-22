# program_8_7.py
'''
Pretrazivanje po koordinatnim osima
'''
import matplotlib.pyplot as plt
import program_8_6 as f2d
from program_8_2 import unimodalni
from program_8_3 import zlatni_rez

def koordinatne_osi(f, x0 = [0,0], maxiter = 99, eps = 0.000001, ax = None, korak = 0):
    '''
    f: funkcija cilja
    x0: pocetna tocka
    maxiter: najveci broj iteracija
    eps: preciznost
    ax: objekt subplot za prikaz
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    
    x = x0.copy()
    xm = [0, 0]
    v = [0, 0]

    def f1d(lam):
        px = x[0] + lam * v[0]
        py = x[1] + lam * v[1]
        return f([px, py])

    for i in range (maxiter):
        xs = x.copy()
        for dim in range (2):
            v[dim] = 1
    
            l, u = unimodalni(f1d)
            a, b = zlatni_rez(f1d, l, u, eps)
            lam = (a + b) / 2
            x = [x[0] + lam * v[0], x[1] + lam * v[1]]
            xm[dim] = x.copy()
        
            v[dim] = 0
        if ax and (korak == 0 or korak == i):
            ax.plot([xs[0], xm[0][0]], [xs[1], xm[0][1]], c='k')
            ax.plot([xm[0][0], xm[1][0]], [xm[0][1], xm[1][1]], c='k')
        
        if (x[0] - xs[0])**2 + (x[1] - xs[1])**2 < eps:
            break
    return x

if __name__ == '__main__':
    # odabir funkcije cilja
    f = f2d.rot; konture = f2d.rot_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture, 1)
    x = koordinatne_osi(f, [-2, -2], ax = ax, korak = 0)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
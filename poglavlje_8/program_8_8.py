# program_8_8.py
'''
Powellov algoritam konjugiranih smjerova
'''
import matplotlib.pyplot as plt
import program_8_6 as f2d
from program_8_2 import unimodalni
from program_8_3 import zlatni_rez

def powell(f, x0 = [0,0], maxiter = 99, eps = 0.000001, ax = None, korak = 0):
    '''
    f: funkcija cilja
    x0: pocetna tocka
    maxiter: najveci broj iteracija
    eps: preciznost
    ax: objekt subplot za prikaz
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    
    def f1d(lam):
        px = x[0] + lam * v[0]
        py = x[1] + lam * v[1]
        return f([px, py])

    def min_pravac():
        l, u = unimodalni(f1d)
        a, b = zlatni_rez(f1d, l, u, eps)
        lam = (a + b) / 2
        return lam

    x = x0.copy()
    vm = [[1, 0], [0, 1]]

    for i in range (maxiter):
        xs = x.copy()

        # pretraga po smjeru n
        v = vm[1]
        lam = min_pravac()
        x = [x[0] + lam * v[0], x[1] + lam * v[1]]
        x1 = x.copy()
        if ax and (korak == 0 or korak == i):
            ax.plot([xs[0], x[0]], [xs[1], x[1]], c='k')

        # pretraga po svim smjerovima
        for i in range (2):
            xs = x.copy()
            v = vm[i]
            lam = min_pravac()
            x = [x[0] + lam * v[0], x[1] + lam * v[1]]
            if ax and (korak == 0 or korak == i):
                ax.plot([xs[0], x[0]], [xs[1], x[1]], c='k')

        # azuriranje skupa smjerova
        vm[0] = vm[1].copy()
        vm[1] = [x[0] - x1[0], x[1] - x1[1]]
    
        if (x[0] - xs[0])**2 + (x[1] - xs[1])**2 < eps:
            break
    return x

if __name__ == '__main__':
    # odabir funkcije cilja
    f = f2d.rosenbrock; konture = f2d.rosenbrock_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture, 1)
    x = powell(f, [-1, -1], ax = ax)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
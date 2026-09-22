# program_8_15.py
'''
Algoritam po Box-u za probleme s ograničenjima
'''
import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np
import program_8_6 as f2d

def crtaj_nejednakost(g, ax, xd = -4, xg = 4):
    xvec = np.linspace(xd, xg, 200); yvec = np.linspace(xd, xg, 200)
    x1, x2 = np.meshgrid(xvec, yvec)
    g0cont = -g([x1, x2])
    cg1 = ax.contour(x1, x2, g0cont, [0], colors='sandybrown')
    cg1.set(path_effects=[patheffects.withTickedStroke(angle=135)])

def provjeri_ogranicenja(x, granice, ogranicenja):
    eksplicitna = all(granice[i][0] <= x[i] <= granice[i][1] for i in range(len(x)))
    nejednakosti = all(ogranicenje(x) >= 0 for ogranicenje in ogranicenja)
    return eksplicitna and nejednakosti

def popravi_tocku(x, granice, ogranicenja, xc):
    xn = np.array([np.clip(x[i], granice[i][0], granice[i][1]) for i in range(len(x))])
    while not all(ogranicenje(xn) >= 0 for ogranicenje in ogranicenja):
        xn = 0.5 * (xn + xc)
    return xn

def box(func, granice, ogranicenja, x0, maxiter=99, br_tocaka=4, eps=1e-6, ax = None, korak = 0):
    '''
    func: funkcija cilja
    x0: pocetna tocka - mora zadovoljavati ogranicenja!
    granice: eksplicitna ogranicenja [(x0_min, x0_max), (x1_min, x1_max)]
    ogranicenja: vektor funkcija ogranicenja nejednakosti
    maxiter: najveci broj iteracija
    br_tocaka: ukupni broj tocaka skupa
    eps: preciznost
    ax: objekt subplot za prikaz
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    # izgradi pocetni skup tocaka
    tocke = [np.array(x0)]; x_c = np.array(x0)
    while len(tocke) < br_tocaka:
        xn = np.array([np.random.uniform(low, high) for low, high in granice])
        while not provjeri_ogranicenja(xn, granice, ogranicenja):
            xn = 0.5 * (xn + x_c)
        tocke.append(xn)
        x_c = np.mean(tocke, axis=0)

    for i in range(maxiter):
        tocke = sorted(tocke, key=func) # ocijeni i uredi po funkciji cilja

        if ax and korak == i:
            for point in tocke:
                ax.scatter(point[0], point[1], color='black')
            ax.scatter(tocke[-1][0], tocke[-1][1], color='gray')

        x_h = tocke[-1]                     # najgora tocka
        x_c = np.mean(tocke[:-1], axis=0)   # novi centroid
        x_r = 2.3 * x_c - 1.3 * x_h         # operacija refleksije

        # provjera ogranicenja
        if not provjeri_ogranicenja(x_r, granice, ogranicenja):
            x_r = popravi_tocku(x_r, granice, ogranicenja, x_c)

        # ako je i dalje najgora, pomakni prema centroidu
        if func(x_r) > func(tocke[-2]):
            x_r = 0.5 * (x_r + x_c)
        tocke[-1] = x_r

        if ax and (korak == 0 or korak == i):
            ax.scatter(x_c[0], x_c[1], color='blue')

        if np.max([np.abs(func(tocke[i]) - func(x_c)) for i in range(1, br_tocaka)]) < eps:
            break

    return tocke[0]

# definicija ogranicenja nejednakosti
def g0(x):
    return (x[0]-0.1) - x[1]**2
def g1(x):
    return x[1]

# eksplicitna ogranicenja
granice = [(-3, 3), (-3, 3)]

if __name__ == '__main__':
    # odabir funkcije cilja
    f = f2d.sferna; konture = f2d.sferna_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture, zoom=3)

    # definicija i crtanje skupa ogranicenja
    ogranicenja = [g0, g1]
    for c in ogranicenja:
        crtaj_nejednakost(c, ax)    

    x0 = [2, 1]
    x = box(f, granice, ogranicenja, x0, ax = ax)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
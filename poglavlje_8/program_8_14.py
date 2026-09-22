# program_8_14.py
'''
Optimizacija problema s ograničenjima metodom kazne i barijere
'''
import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np
import program_8_6 as f2d
from program_8_10 import nelder_mead

# definicija ogranicenja nejednakosti
def g0(x):
    return (x[0]-1) + x[1]**2
def g1(x):
    return x[1]

# definicija ogranicenja jednakosti
def h0(x):
    return x[1] - x[0] - 0

def crtaj_nejednakost(g, ax, xd = -4, xg = 4):
    xvec = np.linspace(xd, xg, 200); yvec = np.linspace(xd, xg, 200)
    x1, x2 = np.meshgrid(xvec, yvec)
    g0cont = -g([x1, x2])
    cg1 = ax.contour(x1, x2, g0cont, [0], colors='sandybrown')
    cg1.set(path_effects=[patheffects.withTickedStroke(angle=135)])

def crtaj_jednakost(h, ax, xd = -4, xg = 4):
    xvec = np.linspace(xd, xg, 100); yvec = np.linspace(xd, xg, 100)
    x1, x2 = np.meshgrid(xvec, yvec)
    h0cont = h([x1, x2])
    ax.contour(x1, x2, h0cont, [0], colors='black')
    
# nadomjesna funkcija cilja
def F(x):
    value = f(x)
    for h in jednakosti:
        value += t * (h(x))**2
    for g in nejednakosti:
        if (g(x)) > 0:
            value -= 1/t * np.log(g(x))
        else:
            value = float('inf')
    return value

if __name__ == '__main__':
    f = f2d.sferna; konture = f2d.sferna_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture)
    nejednakosti = [g0, g1]; jednakosti = [h0]
    for g in nejednakosti:
        crtaj_nejednakost(g, ax)
    for h in jednakosti:
        crtaj_jednakost(h, ax)
    
    t = 1 # pocetna vrijednost parametra t
    x0 = [3, 0]
    x = nelder_mead(F, x0)
    while (x[0] - x0[0])**2 + (x[1] - x0[1])**2 > 10e-12:
        print(f't: {t}, minimum: {x}')
        ax.scatter(x0[0], x0[1], color='blue')
        ax.plot([x0[0], x[0]], [x0[1], x[1]], color='green')
        t *= 100
        x0 = x
        x = nelder_mead(F, x0)

    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
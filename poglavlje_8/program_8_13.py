# program_8_13.py
'''
Kvazi-Newtonov Davidon-Fletcher-Powellov postupak
'''
import numpy as np
import matplotlib.pyplot as plt
import program_8_6 as f2d
from program_8_2 import unimodalni
from program_8_3 import zlatni_rez

def DFP(f, df, x0 = [0.,0.], maxiter = 99, eps = 0.000001, ax = None, korak = 0):
    '''   Davidon-Fletcher-Powellov postupak (kvazi-Newton)
    f: funkcija cilja
    df: prva derivacija funkcije cilja
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

    x = np.array(x0, dtype=float); x0 = np.array(2) 
    dx = np.array(2); dg = np.array(2); v = np.array([0., 0.])
    M = np.zeros((2,2)); N = np.zeros((2,2))
    G = np.eye(2)
    
    for i in range (maxiter):
        x0 = x.copy()
        gf = np.array(df(x)[0])
        v = -G @ gf
    
        l, u = unimodalni(f1d)
        a, b = zlatni_rez(f1d, l, u)
        l = (a + b) / 2
        x[:] = [x[0] + l * v[0], x[1] + l * v[1]]
            
        dx = x - x0
        gf0 = gf.copy()
        gf = np.array(df(x)[0])
        dg = gf - gf0
        M = np.outer(dx, dx) / np.dot(dg, dx)
        N = G @ np.outer(dg, dg) @ G / (dg.T @ G @ dg)
        G = G + M - N
     
        if ax and (korak == 0 or korak == i):
            ax.scatter(x0[0], x0[1])
            ax.plot([x0[0], x[0]], [x0[1], x[1]], color='black')
        
        if abs(x[0] - x0[0]) + abs(x[1] - x0[1]) < eps:
            break
        
    return x

if __name__ == '__main__':
    # odabir funkcije cilja i pripadne derivacije
    f = f2d.rosenbrock; df = f2d.rosenbrock_d; konture = f2d.rosenbrock_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture)
    x = DFP(f, df, [-1, -1], ax = ax)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
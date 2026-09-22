# program_8_11.py
'''
Postupak najbržeg (gradijentnog) spusta
'''
import matplotlib.pyplot as plt
import program_8_6 as f2d
from program_8_2 import unimodalni
from program_8_3 import zlatni_rez

def najbrzi_spust(f, df, x0 = [0,0], maxiter = 99, eps = 0.000001, step = 0, ax = None, korak = 0):
    '''
    f: funkcija cilja
    df: derivacija funkcije cilja
    x0: pocetna tocka
    maxiter: najveci broj iteracija
    eps: preciznost
    step: trazenje minimuma na pravcu (0) ili pomak za zadani dio gradijenta (>0)
    ax: objekt subplot za prikaz
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    def f1d(lam):
        px = x[0] + lam * v[0]
        py = x[1] + lam * v[1]
        return f([px, py])
    
    x = x0
    for i in range (maxiter):
        x0 = x.copy()
        v = df(x)[0]
        if step == 0:
            l, u = unimodalni(f1d)
            a, b = zlatni_rez(f1d, l, u)
            l = (a + b) / 2
            x = [x[0] + l * v[0], x[1] + l * v[1]]
        else:
            x = [x[0] - v[0]*step, x[1] - v[1]*step]

        if ax and (korak == 0 or korak == i):
            #ax.scatter(x0[0], x0[1])
            ax.plot([x0[0], x[0]], [x0[1], x[1]], color='black')

        if (x[0] - x0[0])**2 + (x[1] - x0[1])**2 < eps:
            break

    return x

if __name__ == '__main__':
    # odabir funkcije cilja i pripadne derivacije
    f = f2d.rot; df = f2d.rot_d; konture = f2d.rot_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture, zoom = 1.)
    init = [3, -2]
    x = najbrzi_spust(f, df, init, ax = ax)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
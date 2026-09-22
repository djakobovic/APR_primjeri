# program_8_4.py
'''
Pronalazenje minimuma kvadratnom interpolacijom
'''
import numpy as np
import matplotlib.pyplot as plt
import program_8_1 as f1d

fig,ax = plt.subplots()

def kvadratna_interpolacija(f, a, b, eps = 0.001, koraci = 0):
    '''
    f: funkcija cilja
    a, b: donja i gornja granica unimodalnog intervala
    eps: preciznost
    koraci: ispis svakog koraka postupka
    '''

    def tjeme_parabole(a, b, c):
        '''
        Tjeme parabole kojom se aproksimira unimodalna funkcija f(x)
        u intervalu (a,b) uz zadanu tocku c unutar tog intervala
        '''
        brojnik = (c**2-b**2)*f(a)+(a**2-c**2)*f(b)+(b**2-a**2)*f(c)
        nazivnik = (c-b)*f(a)+(a-c)*f(b)+(b-a)*f(c)
        return brojnik/(2*nazivnik)

    c = (a+b)/2
    d = tjeme_parabole(a,b,c)
    ds = a

    i = 1
    while True:
        x = np.linspace(d-3,d+3,50)
        plt.plot(x, (x-d)**2 + f(d), lw=0.5, ls='--')
        plt.plot(d, f(d),'ko',ms=2)
        if koraci == 1:
            print(f'{i:2d}.iter  a = {a:7.4f}  b = {b:7.4f}   c = {c:7.4f}')
            print(f'd = {d:7.4f}')
        if np.abs(d - ds) < eps or i > 90:
            break

        if d < c and f(d) < f(c):
            a = a; b = c; c = d
        elif d < c and f(d) > f(c):
            a = d; b = b; c = c
        elif d > c and f(d) < f(c):
            a = c; b = b; c = d
        else:
            a = a; b = d; c = c
        i += 1
        ds = d;
        d = tjeme_parabole(a,b,c)
    return d

if __name__ == '__main__':
    print('Pronalazenje minimuma kvadratnom interpolacijom')
    f, ime = f1d.f7, f1d.f7_ime
    #f, ime = f1d.f8, f1d.f8_ime
    a = -1;  b = 3; eps = 0.001
    f1d.crtaj_funkciju(ax, f, ime, a-1, b+1)
    x_min = kvadratna_interpolacija(f, a, b, eps, 1)
    print(f'x_min = {x_min:g}')
    ax.axvline(x_min, c='k',ls='--',lw=0.8)
    ax.plot(x_min, f(x_min),'ko',ms=4)
    plt.show()
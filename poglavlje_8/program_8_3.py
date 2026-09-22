# program_8_3.py
'''
Algoritam zlatnog reza
'''
import matplotlib.pyplot as plt
import program_8_1 as f1d
from program_8_2 import unimodalni

def zlatni_rez(f, a, b, eps = 0.001, koraci = 0):
    '''
    f: funkcija cilja
    a, b: donja i gornja granica unimodalnog intervala
    eps: preciznost
    koraci: ispis svakog koraka postupka
    '''
    
    k = (-1 + 5**0.5) / 2
    d = a + (b - a) * k
    c = b - (b - a) * k
    fc = f(c)
    fd = f(d)

    i = 0
    while (b - a) > eps :
        if fc < fd:
            b = d; d = c
            fd = fc
            c = b - k * (b - a)
            fc = f(c)
        else:
            a = c; c = d
            fc = fd
            d = a + k * (b - a)
            fd = f(d)
        i += 1
        if koraci == 1:
            print(f'{i:2d}.iter  a = {a:6.4f}  c = {c:6.4f}  d = {d:6.4f}  b = {b:6.4f}')
    return (a, b)

if __name__ == '__main__':
    f, ime = f1d.f1, f1d.f1_ime
    x0 = 0
    a, b = unimodalni(f, x0)
    print(f'Pocetne granice intervala: [{a}, {b}]')
    c, d = zlatni_rez(f, a, b, eps = 0.00001, koraci = 0)
    print(f'Konacne granice intervala: [{c:g}, {d:g}]')
    fig,ax = plt.subplots()
    f1d.crtaj_funkciju(ax, f, ime, a-1, b+1)
    ax.axvline((c + d)/2, c='k',ls='--',lw=0.8)
    ax.plot((c + d)/2, f((c + d)/2),'ko',ms=4)
    plt.show()

# program_8_5.py
'''
Primjer minimizacije iz razlicitih pocetnih tocaka
'''
import matplotlib.pyplot as plt
import program_8_1 as f1d
from program_8_2 import unimodalni
from program_8_3 import zlatni_rez

if __name__ == '__main__':
    f, ime = f1d.f4, f1d.f4_ime # odabir funkcije cilja
    xs = [-2, 0, 1] # niz pocetnih tocaka pretrazivanja

    fig,ax = plt.subplots()
    for x0 in xs:
        ax.plot(x0, f(x0),'b+')
        a, b = unimodalni(f, x0, 0.5)
        ax.axvline(a, c='b',ls=':',lw=0.5)
        ax.axvline(b, c='b',ls=':',lw=0.5)
        print(f'Pocetne granice intervala: [{a}, {b}]')
        c, d = zlatni_rez(f, a, b, eps = 0.001, koraci = 0)
        print(f'Konacne granice intervala: [{c:g}, {d:g}]')
        f1d.crtaj_funkciju(ax, f, ime, a-1, b+1)
        ax.axvline((c + d)/2, c='k',ls='--',lw=0.8)
        ax.plot((c + d)/2, f((c + d)/2),'ko',ms=4)
    plt.show()

# program_8_2.py
'''
Pronalazenje pocetnog unimodalnog intervala
'''
import matplotlib.pyplot as plt
import program_8_1 as f1d

def unimodalni(f, x0 = 0, h = 1):
    '''
    f: funkcija cilja
    x0: pocetna tocka
    h: pocetni korak
    '''
    
    step = 1
    l = x0 - h
    m = x0
    r = x0 + h
    fm = f(m); fl = f(l); fr = f(r)

    if fm < fr and fm < fl:
        return (l, r)
    elif fm > fr:
        while True:
            l = m; m = r; fm = fr
            step *= 2
            r = x0 + h * step
            fr = f(r)
            if fm <= fr:
                break
    else:
        while True:
            r = m; m = l; fm = fl
            step *= 2
            l = x0 - h * step
            fl = f(l)
            if fm <= fl:
                break
    return (l, r)

if __name__ == '__main__':
    f, ime = f1d.f11, f1d.f11_ime # odabir funkcije cilja iz zbirke
    x0 = 0
    a, b = unimodalni(f, x0, 1)
    print(f'Granice unimodalnog intervala: [{a}, {b}]')
    fig,ax = plt.subplots()
    f1d.crtaj_funkciju(ax, f, ime, a-1, b+1)
    ax.axvline(a, c='k',ls='--',lw=0.8)
    ax.axvline(b, c='k',ls='--',lw=0.8)
    ax.plot(x0,f(x0),'k+',ms=4)
    plt.show()

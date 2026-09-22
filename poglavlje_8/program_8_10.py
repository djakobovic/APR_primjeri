# program_8_10.py
'''
Simpleks algoritam po Nelderu i Meadu
'''
import matplotlib.pyplot as plt
import program_8_6 as f2d

def nelder_mead(fun, x0 = [0,0], maxiter = 99, eps = 0.000001, ax = None, korak = 0):
    '''
    fun: funkcija cilja
    x0: pocetna tocka
    maxiter: najveci broj iteracija
    eps: preciznost
    ax: objekt subplot za prikaz
    korak: prikaz zadane iteracije (0 prikazuje sve)
    '''
    def centroid(x, h):
        xc = [0, 0]
        for i in range(3):
            if i != h:
                xc[0] += x[i][0] / 2
                xc[1] += x[i][1] / 2
        return xc
    def refleksija(xc, xh):
        xr = [0, 0]
        for i in range(2):
            xr[i] = (1 + alpha) * xc[i] - alpha * xh[i]
        return xr
    def ekspanzija(xr, xc):
        xe = [0, 0]
        for i in range(2):
            xe[i] = (1 - gamma) * xc[i] + gamma * xr[i]
        return xe
    def kontrakcija(xc, xh):
        xk = [0, 0]
        for i in range(2):
            xk[i] = (1 - beta) * xc[i] + beta * xh[i]
        return xk
    def pomak(x, l):
        for i in range(3):
            x[i][0] = (x[i][0] + x[l][0]) / 2
            x[i][1] = (x[i][1] + x[l][1]) / 2

    # pretpostavljeni parametri i simpleks od 3 tocke
    alpha = 1; beta = 0.5; gamma = 2
    x = list(range(3))
    f = list(range(3))
    x[0] = x0; x[1] = x[0].copy(); x[2] = x[0].copy()
    x[1][0] += 1; x[2][1] += 1

    for it in range (maxiter):
        for i in range(3):
            f[i] = fun(x[i])
        h = l = 0
        for i in range(3):
            if f[i] > f[h]:
                h = i
            if f[i] < f[l]:
                l = i
            
        xc = centroid(x, h)
        xr = refleksija(xc, x[h])
        fr = fun(xr)

        if ax and (korak == 0):
            ax.scatter(x[l][0], x[l][1], color='blue')
        if ax and (korak == it):
            for i in range(3):
                ax.scatter(x[i][0], x[i][1], color='green')
                j = (i+1) % 3
                ax.plot([x[i][0], x[j][0]], [x[i][1], x[j][1]], color='green')
            ax.scatter(xc[0], xc[1], color='red')
            ax.scatter(xr[0], xr[1])
        
        if fr < f[l]:
            xe = ekspanzija(xr, xc)
            if ax and (korak == it):
                ax.scatter(xe[0], xe[1])
            fe = fun(xe)
            if fe < f[l]:
                x[h] = xe
            else:
                x[h] = xr
        else:
            worse = 1
            for i in range(3):
                if fr < f[i]:
                    worse = 0
                    break
            if worse == 1:
                if fr < f[h]:
                    x[h] = xr
                xk = kontrakcija(xc, x[h])
                if ax and (korak == it):
                    ax.scatter(xk[0], xk[1], color='black')
                fk = fun(xk)
                if fk < f[h]:
                    x[h] = xk
                else:
                    pomak(x, l)
            else:
                x[h] = xr

        d = ((x[h][0]-xc[0])**2 + (x[h][1]-xc[1])**2)**0.5
        if abs(f[l] - f[h]) < eps and d < eps:
            break

    return x[l]

if __name__ == '__main__':
    # odabir funkcije cilja
    f = f2d.rosenbrock; konture = f2d.rosenbrock_konture
    fig,ax = plt.subplots()
    f2d.crtaj_konture(ax, f, konture)
    x = nelder_mead(f, [-1.9,2.1], ax = ax, korak = 0)
    print(f'Rezultat: f({x}) = {f(x)}')
    plt.show()
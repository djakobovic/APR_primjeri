# program_8_6.py
'''
Definicija i crtanje kontura 2D funkcija
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

'''
Sferna funkcija
'''
def sferna(x):
    return 1*x[0]**2. + 1*x[1]**2.
def sferna_konture():
    xd, xg, broj = -4, 4, 201
    razine = np.array([0.2,1.0,4.0,10.0,20.0,30.0,40.0])
    naslov = r'$Sferna$'+' '+r'$funkcija$'
    funkcija =r'$f(x_0,x_1)=x_0^2+x_1^2$'
    min = [(0, 0)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Rotirana sferna funkcija
'''
def rot(x):
    return (x[0] - 0)**2 + (x[1] - 0)**2 + 1.5 * (x[0] - 0) * (x[1] - 0)
def rot_konture():
    xd, xg, broj = -3, 3, 201
    razine = np.array([0.2,1.0,4.0,10.0,20.0,30.0,40.0])
    naslov = r'$Rotirana$'+' '+r'$funkcija$'
    funkcija =r'$f(x_0,x_1)=x_0^2+x_1^2+1.5x_0x_1$'
    min = [(0, 0)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Rosenbrockova funkcija
'''
def rosenbrock(x):
    return (1 - x[0])**2. + 100 * (x[1] - x[0]**2.)**2.
def rosenbrock_konture():
    xd, xg, broj = -3, 5, 201
    razine = np.array([1.0,10.,100.,1000.,2000.0,5000.0,10000.0,20000.])
    naslov = r'$Rosenbrockova$'+' '+r'$funkcija$'
    funkcija =r'$f(x_0,x_1)=100*(x_1-x_0^2)^2+(1-x_0)^2$'
    min = [(1, 1)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Boothova funkcija
'''
def booth(x):
    return (x[0]+2*x[1]-7)**2+(2*x[0]+x[1]-5)**2
def booth_konture():
    xd, xg, broj = -1, 5, 201
    razine = np.array([10.,20.,50.,100.,200.0,500.,1000.0,1500.0,2000.])
    naslov = r'$Boothova$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=(x_0+2x_1-7)^2+(2x_0+x_1-5)^2$'
    min = [(1,3)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Matyasova funkcija
'''
def matyas(x):
    return 0.26*(x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]
def matyas_konture():
    xd, xg, broj = -8, 8, 201
    razine= np.array([1.0,5.0,10.,20.,50.0,100.0,150.0,200.0,400.0,600.])
    naslov = r'$Matyasova$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=0.26(x_0^2+x_1^2)-0.48x_0x_1$'
    min = [(0, 0)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Trogrba funkcija
'''
def trogrba(x):
    return 2*x[0]**2 - 1.05*x[0]**4 + x[0]**6/6 +x[0]*x[1] + x[1]**2
def trogrba_konture():
    xd, xg, broj = -2.5, 2.5, 201
    razine = np.array([0.5, 1.0, 2.0, 5.0, 10.,20.])
    naslov = r'$Trogrba$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=2x_0^2-1.05x_0^4 + x_0^6/6 + x_0x_1 + x_1^2$'
    min = [(0,0), (-1.74755, 0.873776), (1.74755, -0.873776)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Himmelblauova funkcija
'''
def himmel(x):
    return (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2
def himmel_konture():
    xd, xg, broj = -5, 5, 201
    razine= np.array([1.0,5.0,10.,20.,50.0,100.0,150.0,200.0,400.0,600.])
    naslov = r'$Himmelblauova$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=(x_0^2+x_1-11)^2+(x_0+x_1^2-7)^2$'
    mins = [(3, 2), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848126)]
    return xd, xg, broj, razine, naslov, funkcija, mins
'''
Bird funkcija (ptičje gnijezdo)
'''
def bird(x):
    return (x[0]-x[1])**2+np.cos(x[0])*np.exp(1-np.sin(x[1]))**2+np.sin(x[1])*np.exp(1-np.cos(x[1]))**2
def bird_konture():
    xd, xg, broj = -2*np.pi,3,301
    razine= np.array([-100.,-75.0,-50.0,-25.0,-10.0,0.0,10.0,25.0,50.0,75.0,100.0,150.0,200.0])
    naslov = r'$Bird$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=(x_0-x_1)^2+\sin(x_0)e^{[1-\cos(x_1)]^2}+\cos(x_1)e^{[1-\sin(x_0)]^2}$'
    min = [(-3.1302468,-1.5821422)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Bealeova funkcija
'''
def beale(x):
    return (x[0]*x[1]-x[0]+1.5)**2+(x[0]*x[1]**2-x[0]+2.25)**+2+(x[0]*x[1]**3-x[0]+2.625)**2
def beale_konture():
    xd, xg, broj = -2, 4, 201
    razine= np.array([0.1,0.5,1.0,5.0,10.0,50.0,100.0])
    naslov = r'$Bealova$'+' '+r'$funkcija$'
    funkcija = r'$f(x_0,x_1)=(x_0x_1-x_1+1.5)^2+(x_0x_1^2-x_0+2.25)^2+(x_0x_1^2-x_0+2.265)^2$'
    min = [(3, 0.5)]
    return xd, xg, broj, razine, naslov, funkcija, min
'''
Funkcija tuljca f(x_0,x_1)=sin(sqrt(x_0**2+x_1**2))
'''
def tuljac(x):
    return np.sin(np.sqrt(x[0]**2+x[1]**2))
def tuljac_konture():
    xd, xg, broj = -np.pi,np.pi,301
    razine = np.array([-1.0,-0.70,-0.50,-0.25,0.00,0.25,0.5,0.80,0.90,0.99])
    naslov = r'$Funkcija$'+' '+r'$tuljca$'
    funkcija = r'$f(x_0,x_1)=\sin(\sqrt{x_0^2+x_1^2} )}$' 
    min = []
    return xd, xg, broj, razine, naslov, funkcija, min


'''
Konstrukcija kontura ili ploha zadane funkcije
'''
def crtaj_konture(ax, f, konture, zoom = 1):
    plt.rc('mathtext',fontset='stix')
    ax.grid(True)
    xd, xg, broj, razine, naslov, funkcija, mins = konture()
    if zoom != 1:
        mid = (xd + xg)/2
        xd, xg = mid - (mid - xd)/zoom, mid + (xg - mid)/zoom
        razine = razine / zoom
        ax.set_xlim(xd, xg)
        ax.set_ylim(xd, xg)
    X_0, X_1 = np.meshgrid(np.linspace(xd,xg,broj), np.linspace(xd,xg,broj))
    F = f([X_0, X_1])
    ax.set(aspect='equal', xlabel=r'$x_0$',ylabel=r'$x_1$')
    ax.set_title(naslov+': '+funkcija,fontsize=12) 
    kontura=ax.contour(X_0, X_1, F, levels=razine, colors='k',linewidths=0.4,
                       linestyles='-')
    ax.clabel(kontura,inline=True,fontsize=8)
    for min in mins:
        ax.plot(min[0], min[1],'r+')
    return

def crtaj_plohe(ax, f, konture):
    xd, xg, broj, razine, naslov, funkcija, mins = konture()
    X_0, X_1 = np.meshgrid(np.linspace(xd,xg,broj), np.linspace(xd,xg,broj))
    F = f([X_0, X_1])
    ax.plot_surface(X_0, X_1, F, cmap='viridis')
    ax.set(xlabel=r'$x_0$',ylabel=r'$x_1$',zlabel=r'$f(x_0,x_1)$')
    return


# derivacije odabranih funkcija
def sferna_d(x):
    opt = [0, 0]; a = 1; b = 1
    return [2*a*(x[0]-opt[0]), 2*b*(x[1]-opt[1])], [[2*a, 0], [0, 2*b]]

def rot_d(x):
    opt = [0, 0]
    return [x[1] + 2*(x[0]-opt[0])-opt[1], x[0] + 2*(x[1]-opt[1])-opt[0]], []

def rosenbrock_d(x):
    return [-2*(1-x[0])-400*x[0]*(x[1]-x[0]**2), 200*(x[1]-x[0]**2)], [[2-400*(x[1]-3*x[0]**2), -400*x[0]], [-400*x[0], 200]]

def jak_d(x):
    return [(2*x[0]**3-2*x[0]*x[1]**2) / (abs(x[0]-x[1])*abs(x[0]+x[1])) + x[0] / (x[0]**2+x[1]**2)**0.5, 
            (2*x[1]**3-2*x[1]*x[0]**2) / (abs(x[0]-x[1])*abs(x[0]+x[1])) + x[1] / (x[0]**2+x[1]**2)**0.5]
def nr(x):
    return x[0]**4/4 - x[0]**2 + 2*x[0] + (x[1]-1)**2
def nr_d(x):
    return [x[0]**3 - 2*x[0] + 2, 2*x[1] - 2], [[3*x[0]**2 - 2, 0], [0, 2]]
def nr_konture():
    xd, xg, broj = -3, 4, 201
    razine = np.array([0.1,0.5,1.0,2.0,5.0,10.0,15.0,30.0])
    naslov = r''
    funkcija =r'$f(x_0,x_1)=x_0^4/4 - x_0^2 + 2x_0 + (x_1-1)^2$'
    min = [(-1.7693, 1)]
    return xd, xg, broj, razine, naslov, funkcija, min

if __name__ == '__main__':
    fig = plt.figure(figsize=(10, 5), layout='constrained')
    ax = fig.add_subplot(122)
    ax3d = fig.add_subplot(121, projection='3d')
    # odabir funkcije za prikaz:
    crtaj_konture(ax, nr, nr_konture)
    crtaj_plohe(ax3d, nr, nr_konture)
    plt.show()
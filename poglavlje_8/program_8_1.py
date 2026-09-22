# program_8_1.py
'''
    Zbirka s 12 funkcija jedne varijable prikazane u intervalima [a,b]
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

f1_ime = r'$(x - 2)x(x + 2)^2$'
def f1(x):
	return (x - 2)*x*(x + 2)**2
f2_ime = r'$\frac{-6}{(x-1)^2+2}$'
def f2(x):
	return - 6/((x-1)**2 + 2)
f3_ime = r'$-(x+\sin(x))e^{-x^2}$'
def f3(x):
	return -(x + np.sin(x)) * np.exp(-x**2)
f4_ime = r'$\sin(x)+\sin{\frac{10}{3}x}$'
def f4(x):
	return np.sin(x)+np.sin((10/3)*x)
f5_ime = r'$\frac{2}{3}x^3+\frac{3}{2}x^2-2x-1$'
def f5(x):
	return (2/3)*x**3 +(3/2)*x**2 - 2*x - 1
f6_ime = r'$-(1.4-3.0x)\sin(18.0x)$'
def f6(x):
	return -(1.4-3.0*x)*np.sin(18.0*x)
f7_ime = r'$2\cos(x)+\cos(2x)$'
def f7(x):
        return 2*np.cos(x)+np.cos(2*x)
f8_ime = r'$(\sin x)^3+(\cos x)^3$'
def f8(x):
        return np.sin(x)**3+np.cos(x)**3
f9_ime = r'$-(x\sin(x))$'
def f9(x):
        return -(x * np.sin(x))
f10_ime = r'$-(16x^2-24x+5)e^{-x}$'
def f10(x):
        return -(16*x**2-24*x+5)*np.exp(-x)
f11_ime = r'$\frac{x^2-5x+6}{x^2+1}$'
def f11(x):
        return (x**2-5*x+6)/(x**2+1)
f12_ime = r'$-e^{-x}\sin({2\pi}x)$'
def f12(x):
        return -np.exp(-x)*np.sin(2*np.pi*x)


def crtaj_funkciju(ax, f, naziv, xd = -3, xg = 3, broj = 200):
	xp = np.linspace(xd,xg,broj)
	ax.set(title=naziv,xlabel=r'$x$',ylabel='$y$')
	ax.plot(xp,f(xp),c='k',lw=0.5)


if __name__ == '__main__':
	# prvi list (Figure1)
	fig,axs = plt.subplots(3,2,figsize=(5,6),layout='constrained')
	crtaj_funkciju(axs[0,0], f1, f1_ime, -3, 3)
	crtaj_funkciju(axs[0,1], f2, f2_ime, -3, 3)
	crtaj_funkciju(axs[1,0], f3, f3_ime, -3, 8)
	crtaj_funkciju(axs[1,1], f4, f4_ime, -3, 3)
	crtaj_funkciju(axs[2,0], f5, f5_ime, -3, 3)
	crtaj_funkciju(axs[2,1], f6, f6_ime, 0, 1.2)

	# drugi list (Figure2)
	fig,axs = plt.subplots(3,2,figsize=(5,6),layout='constrained')
	crtaj_funkciju(axs[0,0], f7, f7_ime, -np.pi/2, 2*np.pi)
	crtaj_funkciju(axs[0,1], f8, f8_ime, 0.0, 2*np.pi)
	crtaj_funkciju(axs[1,0], f9, f9_ime, -5, 5)
	crtaj_funkciju(axs[1,1], f10, f10_ime, 2, 4)
	crtaj_funkciju(axs[2,0], f11, f11_ime, -6, 6)
	crtaj_funkciju(axs[2,1], f12, f12_ime, 0, 4)

	plt.show()

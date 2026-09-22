# program_5_3.py
'''
Amplitudna i fazna karakteristika RC filtra
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

R = 1.25
C = 0.25*10**-3
omega_g = 1/(R*C)
print(f'R = {R} om\nC = {C} farad')
print(f'omega_g = {omega_g}')

omega = np.arange(10*1,10**6,0.1)

if __name__ == '__main__':
    fig,(ax0,ax1) = plt.subplots(2,1,figsize=(4,5),layout='constrained')

    ax0.set(title=r'$RC$'+' '+r'$filtar$',ylabel=r'$amplituda$')
    Z_R = R + 0j
    Z_C = 0 - (1/(omega*C))*1j    
    amplituda = np.abs(Z_C/(Z_R + Z_C))
    ax0.semilogx(omega,amplituda,'k-',lw=1.0)
    ax0.axvline(x = omega_g,c='r',ls=':',lw=1.0)
    ax0.text(1.7*10**3,0.05,r'$\omega_g$')
    ax0.axhline(y = 1/np.sqrt(2),c='r',ls=':',lw=1.0)
    ax0.text(8,0.62,r'$0.707$')
    ax0.grid()

    ax1.set(xlabel=r'$kutna$'+' '+r'$frekvencija$'+' '+r'$\omega$',
            ylabel=r'$fazni$'+' '+r'$pomak$'+' '+r'$[stupnjevi]$')
    fazni_pomak = np.angle(Z_C/(Z_R + Z_C),deg=True)
    ax1.semilogx(omega,fazni_pomak,'b--',lw=1.0)
    ax1.grid()

    fig.savefig('sl.5.12.pdf')
    fig.show()

# program_5_5.py
'''
Granične grekvencije LCR filtara
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

L = 5*10**-3
C = 2*10**-6
R = np.array([1,10,50,100,200])
legenda = np.array([r'$R=1$',r'$R=10$',r'$R=50$',r'$R=100$',r'$R=200$'])
omega_res = np.sqrt(1/(L*C))
print(f'L = {L:5.0e}   C = {C:5.0e}\nomega_res = np.sqrt(1/(L*C)) = {omega_res:5.0e}\n')

if __name__ == '__main__':
    omega = np.arange(10**3,10**5,1.0)

    fig,ax = plt.subplots()
    ax.set(title=r'$Granične$'+' '+r'$frekvencije$'+' '+
           r'$LCR$'+' '+r'$filtara$',
           xlabel=r'$kutna$'+' '+r'$frekvencija$'+' '+r'$\omega$',
           ylabel=r'$amplituda$') 
    for i in range(5):
        Z_R = R[i] + 0j
        Z_RLC = R[i]+ (omega*L - 1/(omega*C))*1j
        amplituda = np.abs(Z_R/(Z_RLC))
        ax.semilogx(omega,amplituda,lw=1.0, label=legenda[i])
        pom = np.sqrt((R[i]/(2*L))**2 +1/(L*C))
        omega_d = pom - R[i]/(2*L)
        omega_g = pom + R[i]/(2*L)
        poj = R[i]/L
        print(f'R = {R[i]:4}  omega_d = {omega_d:4.0f}', end=' ')
        print(f'  omega_g = {omega_g:5.0f}  poj = {poj:5.0f}', end=' ')
        print(f'  R/L = {R[i]/L:5.0f}')
        ax.axvline(x = omega_d, ls='--',lw = 1.0)
        ax.axvline(x = omega_g, ls='--',lw = 1.0)
    ax.legend(loc='lower left')
    ax.axhline(y = 0.707, ls='--',lw = 1.2)
    ax.text(10**3,0.65,r'$0.707$')
 
    fig.savefig('sl.5.15.pdf')
    fig.show()

# program_5_4.py
'''
Amplitudne karakteristike LCR filtara uz različite
vrijednosti otpora R.
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

L = 5*10**-3
C = 2*10**-6
R = np.array([1,10,100,1000,10000])
legenda = np.array([r'$R=10^0$',r'$R=10^1$',r'$R=10^2$',
                    r'$R=10^3$',r'$R=10^4$'])
omega_res = np.sqrt(1/(L*C))
print(f'omega_res = np.sqrt(1/(L*C)) = {omega_res}')                                                                         

if __name__ == '__main__':
    omega = np.arange(1,10**7,1.0)

    fig,ax = plt.subplots()
    ax.set(title=r'$Amplitudne$'+' '+r'$karakteristike$'+' '+
           r'$LCR$'+' '+r'$filtara$',
           xlabel=r'$kutna$'+' '+r'$frekvencija$'+' '+r'$\omega$',
           ylabel=r'$amplituda$')
    for i in range(5):
        Z_R = R[i]+0j    
        Z_RLC = R[i]+ (omega*L - 1/(omega*C))*1j
        amplituda = np.abs(Z_R/(Z_RLC))
        ax.semilogx(omega,amplituda,lw=1.0, label=legenda[i])
    ax.axhline(y = 0.707, ls='--',lw = 1.2)
    ax.text(0.8,0.65,r'$0.707$')
    ax.grid()
    ax.axvline(x = omega_res, ls='-.',lw = 1.2)
    ax.legend(loc='lower left')
    
    fig.savefig('sl.5.14.pdf')
    fig.show()

# program_7_7.py
'''
   Vremensko ponašanje njihala
      d2theta/dt2 = -(g/L)*sin(theta)
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# theta = x1, dtheta/dt = x2
def njihalo(t,x,L):
    x1,x2 = x
    dx1dt = x2
    dx2dt = -(g/L)*np.sin(x1)
    return [dx1dt,dx2dt]

if __name__ == '__main__':   
    fig,axs = plt.subplots(2,2,figsize=(8,6),layout='constrained')

    t_0 = 0; t_f = 3.; m = 1000
    te = np.linspace(t_0,t_f,m)
    L = 1.0
    g = 9.81
    T = 2*np.pi*np.sqrt(L/g)
# Početna vrijednost theta(0) = x1_0    
    x1_0 = 0
    for i in range(4):
        x1_0 += 0.1*np.pi
        sol = solve_ivp(njihalo,[0,t_f],[x1_0,0],method='LSODA',
                        t_eval=te,args=(L,))
        r,s = divmod(i,2)
        theta = sol.y[0, : ]
        axs[r,s].set(title= f'theta(0) = {x1_0:1.3f} radijana',
                     xlim=(0,3),ylim=(-1.5,1.5))
        axs[r,s].plot(te,sol.y[0, : ],lw=1.0)
        axs[r,s].axhline(ls='--',lw=1.0)
        axs[r,s].axvline(T,ls='--',lw=1.0)
        axs[r,s].text(2.05,-1.4,f'T = {T:1.3f}')
    axs[0,0].set(ylabel=f'theta(t)')
    axs[1,0].set(ylabel=f'theta(t)')
    axs[1,0].set(xlabel=f't')
    axs[1,1].set(xlabel=r't')

    fig.savefig('sl.7.12.pdf')
    fig.show()

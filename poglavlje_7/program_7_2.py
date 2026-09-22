# program_7_2.py
'''
Odziv LCR sklopa na skok ulaznog napona 
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def LCRsklop(t,x,R):
    x1,x2 = x
    dx1dt = (1/C)*x2
    dx2dt = -(1/L)*x1 - (R/L)*x2 + K/L
    dxdt = [dx1dt,dx2dt]
    return dxdt

def odziv_LCR(L,C,R):
    R = RJ[j]; r,s = divmod(j,2)
    sol = solve_ivp(LCRsklop,[0,t_f],[0,0],method='LSODA',t_eval=te,args=(R,))
# grafički prikaz ulaznog i izlaznog napona
    axs[r,s].set(title=f'u_ul i u_iz uz L={L}, C={C}, R={R}',
                 xlabel='t',ylabel='u_ul(t),u_iz(t)')
    axs[r,s].plot(te,u_ul,'k--',lw=1.0,label='u_ul')
    u_iz = sol.y[0, : ]
    axs[r,s].plot(te,u_iz,'r-',lw=1.0,label='u_iz')
    axs[r,s].legend(loc='lower right')

if __name__ == '__main__':
    
    fig,axs = plt.subplots(2,2,figsize=(8,6),layout='constrained')

    t_0 = 0; t_f = 100.; m = 1000
    te = np.linspace(t_0,t_f,m)

    L = 5; C = 0.5
    RJ = [10.,1.,0.1,0.0]
    K = 1.
    u_ul = K * np.ones(m)
    for j in range(4):
        R = RJ[j]
        odziv_LCR(L,C,R)

    fig.savefig('sl.7.7.pdf')
    fig.show()

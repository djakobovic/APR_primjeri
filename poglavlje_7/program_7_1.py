# program_7_1.py
'''
Odziv RC sklopa na skok ulaznog napona 
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

t_0 = 0 ; t_f = 3.0
te = np.linspace(t_0,t_f,101)
C = 10**(-3)
K = 1

if __name__ == '__main__':
    fig,(ax0,ax1) = plt.subplots(1,2,figsize=(9,4),layout='constrained')
    ax0.set(title='Odziv RC sklopa na skok veličine K=1',
            xlabel='t', ylabel='u_iz(t)',
            xlim=(t_0,t_f),ylim=(0,K))
    ax1.set(title='Odziv CR sklopa na skok veličine K=1',
            xlabel='t', ylabel='u_iz(t)',
            xlim=(t_0,t_f),ylim=(0,K))

    def rcsklop(t,x,R):
        dxdt = -1/(R*C)*x + K/(R*C)
        return dxdt

# Izlazni naponi uz vremenske konstante RC: 0.25,0.5,1.0,2.0,4.0
    R = 0.125*10**3
    for i in range(1,6):
        R = 2*R
        x_0 = 0
        sol = solve_ivp(rcsklop,[t_0,t_f],[x_0],method='LSODA',t_eval=te,
                        args=[R])
        u_iz_RC = sol.y[0, : ]
        ax0.plot(te,u_iz_RC,lw=1.0,label=f'u_iz uz RC = {R*C}')
        u_iz_CR = K - sol.y[0, : ]
        ax1.plot(te,u_iz_CR,lw=1.0,label=f'u_iz uz RC = {R*C}')
    ax0.legend(loc='lower right')
    ax1.legend(loc='upper right')

    fig.savefig('sl.7.5.pdf')
    fig.show()

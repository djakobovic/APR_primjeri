# program_7_6.py
'''
Rješenja Verhulstove diferencijalne jednadžbe dp(t)/dt = r*p(t)*(1 - p(t)/K)
uz r = 0.1 i K = 1000
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t_0 = 0; t_f = 500.; m = 2000
te = np.linspace(t_0,t_f,m)

def fun(t,x,r,K):
    dxdt = r*x*(1 - (1/K)*x)
    return dxdt

if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(5,4),layout='constrained')

    r = 0.1; K = 1000
    ax.set(title=f'Rješenja jednadžbe\ndp(t)/dt = 0.1*p(t)*(1 - p(t)/1000)',
           xlim = (0,100),ylim=(0,2000), xlabel='t',ylabel='p(t)')
    x_0 = np.array([2.0,50.0,100.0,500.0,1500.0,2000.0])
    for i in range(6):
        sol = solve_ivp(fun,[t_0,t_f],[x_0[i]],method='LSODA',t_eval=te,args=(r,K))
        ax.plot(te,sol.y[0, : ],lw=1.0, label=f'p(0) = {x_0[i]}')
    ax.legend(loc='upper right')

    fig.savefig('sl.7.10.pdf')
    fig.show()

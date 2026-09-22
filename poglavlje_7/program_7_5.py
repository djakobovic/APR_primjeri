# program_7_5.py
'''
Rješenja diferencijalne jednadžbe dx/dt = a*x+b
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t_0 = 0; t_f = 10.; m = 200
te = np.linspace(t_0,t_f,m)

def fun(t,x,a,b):
    dxdt = a*x + b
    return dxdt

if __name__ == '__main__':
    fig,ax = plt.subplots(3,2,figsize=(8,8),layout='constrained')

    x_0 = 10.0
# a = 0, b > 0
    a = 0.0 ;  b = np.array([0.2,0.4,0.6,0.8,1.0]) 
    ax[0,0].set(title=f'Rješenje jednadžbe dx/dt = a*x + b\nuz a = 0, b > 0',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[x_0],method='LSODA',t_eval=te,args=(a,b[i]))
        ax[0,0].plot(te,sol.y[0, : ],lw=1.0,label=f'b = {b[i]}')
    ax[0,0].legend(loc='upper left')
# a = 0, b < 0
    ax[0,1].set(title=f'Rješenje jednadžbe dx/dt = a*x + b\nuz a = 0, b < 0',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[x_0],method='LSODA',t_eval=te,args=(a,-b[i]))
        ax[0,1].plot(te,sol.y[0, : ],lw=1.0,label=f'b = {-b[i]}')
    ax[0,1].legend(loc='lower left')

# a > 0, b = 0
    a = np.array([0.02,0.04,.06,0.08,0.1]);  b = 0.0
    ax[1,0].set(title=f'Rješenje jednadžbe dx/dt = a*x + b\nuz a > 0, b = 0',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[x_0],method='LSODA',t_eval=te,args=(a[i],b))
        ax[1,0].plot(te,sol.y[0, : ],lw=1.0,label=f'a = {a[i]}')
    ax[1,0].legend(loc='upper left')
# a < 0, b = 0
    a = np.array([-0.2,-0.4,-0.6,-0.8,-1.0]);  b = 0.0
    ax[1,1].set(title=f'Rješenje jednadžbe dx/dt = a*x + b\nuz a < 0, b = 0',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[x_0],method='LSODA',t_eval=te,args=(a[i],b))
        ax[1,1].plot(te,sol.y[0, : ],lw=1.0,label=f'a = {a[i]}')
    ax[1,1].legend(loc='upper right')

# a != 0, b !=0
    a = -0.5;  b = -5.
# x_0 < b/a
    x_0 = np.array([0,2,4,6,8])
    ax[2,0].set(title=f'Rješenje jednadžbe dx/dt = - 0.5*x - 5.0\nuz x_0 = 0,2,4,6,8',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[1],method='LSODA',t_eval=te,args=(a,0))
        x_r = (x_0[i] - b/a)*sol.y[0, : ] + b/a
        ax[2,0].plot(te,x_r,lw=1.0,label=f'x_0 = {x_0[i]}')
    ax[2,0].legend(loc='lower right')
# x_0 > b/a
    x_0 = np.array([12,14,16,18,20])
    ax[2,1].set(title=f'Rješenje jednadžbe dx/dt= - 0.5*x - 5.0\nx_0 = 12,14,16,18,20',
                xlabel='t',ylabel='x(t)')
    for i in range(5):
        sol = solve_ivp(fun,[t_0,t_f],[1],method='LSODA',t_eval=te,args=(a,0))
        x_r = (x_0[i] - b/a)*sol.y[0, : ] + b/a
        ax[2,1].plot(te,x_r,lw=1.0,label=f'x_0 = {x_0[i]}')
    ax[2,1].legend(loc='upper right')

    fig.savefig('sl.7.9.pdf')
    fig.show()    

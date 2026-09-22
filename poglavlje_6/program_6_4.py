# program_6_4.py
'''
Program rješava sustav Lotka-Volterra jednadžbi
    dx/dt = a*x - b*x*y
    dy/dt = -c*y + d*x*y
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t_0 = 0.; t_f = 6.
    x_0 = 4.; y_0 = 6.

    def lotkavolterra(t,z,a,b,c,d):
        x, y = z
        return [a*x - b*x*y, -c*y + d*x*y] 

    fig,(ax0,ax1) = plt.subplots(2,1,figsize=(4,5),layout='constrained')

# Rješenje uz parametre a=4, b =1, c =3, d=1
    sol =solve_ivp(lotkavolterra,[t_0,t_f],[x_0,y_0],method='LSODA',
                   args = [4,1,3,1],dense_output = True)
    ax0.set(title='Parametri: a=4, b=1, c=3, d=1',
            xlabel='vrijeme',ylabel='populacija')
    ax0.plot(sol.t,sol.y[0, : ],lw=1.0,label='plijen')
    ax0.plot(sol.t,sol.y[1, : ],lw=1.0,label='predatori')
    ax0.legend(loc='upper right')
    
# Rješenje uz parametre a=4, b =2, c =3, d=2
    sol = solve_ivp(lotkavolterra,[t_0,t_f],[x_0,y_0],method='LSODA',
                    args = [4,2,3,2],dense_output = True)
    ax1.set(title='Parametri: a=4, b=2, c=3, d=2',
            xlabel='vrijeme',ylabel='populacija')
    ax1.plot(sol.t,sol.y[0, : ],lw=1.0,label='plijen')
    ax1.plot(sol.t,sol.y[1, : ],lw=1.0,label='predatori')
    ax1.legend(loc='upper right')

    fig.show()
    fig.savefig('sl.6.13.pdf')

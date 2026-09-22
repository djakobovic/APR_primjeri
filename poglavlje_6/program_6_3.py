# program_6_3.py
'''
   Rješenje diferncijalne jednadžbe
       dx/dt = -0.6*x
   s početnom vrijednošću x_0 = 2 u trenutku t_0 = 0
   u intervalu 0 <= t <= 10 odnosno uz t_0 = 0 i t_f = 10
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t_0 = 0.; t_f = 10.
    x_0 = 2.
    te = np.linspace(t_0,t_f,101)

    def eksp_pad(t,x):
        return -0.6*x

    fig,(ax0,ax1) = plt.subplots(2,1,figsize=(4,5),layout='constrained')    

# Poziv funkcije bez parametra t_eval
    print(f'Rješenje bez parametra t_eval')
    sol = solve_ivp(eksp_pad,[t_0,t_f],[2],method ='LSODA',dense_output=True)
    print(sol)
    t = sol.t; x = sol.y[0, : ]
    ax0.set(title='Poziv funkcije bez parametra t_eval',
           xlabel='t',ylabel='x(t)')
    ax0.plot(t,x,lw=1.0)
# Poziv funkcije s parametrom t_eval
    print(f'\nRješenje s parametrom t_eval')
    sol = solve_ivp(eksp_pad,[t_0,t_f],[2],method ='LSODA',t_eval=te)
    print(sol)
    x = sol.y[0, : ]
    ax1.set(title='Poziv funkcije s parametrom t_eval',
           xlabel='t',ylabel='x(t)')
    ax1.plot(te,x,lw=1.0,)

    fig.savefig('sl.6.12.pdf')
    fig.show()


# primjer_7_9.py
'''
   Rješenje Moore-Spiegelove diferencijalne jednadžbe
   trećeg reda
      d3y/dt3+d2y/dt2 + (a-b+b*y**2)*dy/dt + a*y = 0
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t_0 = 0; t_f = 30; m = 1000
te = np.linspace(t_0,t_f,m)

def MooreSpiegel(t,x,a,b):
    x1,x2,x3 = x
    dx1dt = x2
    dx2dt = x3
    dx3dt = - a*x1 - (a-b+b*x1**2)*x2 - x3
    dxdt = [dx1dt,dx2dt,dx3dt]
    return dxdt

if __name__ == '__main__':
    fig,axs = plt.subplots(2,2,figsize=(8,6),layout='constrained')
    b = 100.
    lista_a = [3, 15, 25, 30]
    for i in range(len(lista_a)):
        a = lista_a[i]
        sol = solve_ivp(MooreSpiegel,[0,t_f],[0.2,0.0,0.0],method='LSODA',
                        t_eval=te,args=(a,b))
        r,s = divmod(i,2)
        y = sol.y[0, : ]
# Grafički prikaz rješenja varijable y(t)
        axs[r,s].set(title=f'Rješenje Moore-Spiegelove jednadžbe'+'\n'+
                        f'uz a = {a:5.1f}, b = {b:5.1f}')
        axs[r,s].plot(te,y,lw=1.0)
        axs[0,0].set(ylabel=f'y(t)')
        axs[1,0].set(ylabel=f'y(t)')
        axs[1,0].set(xlabel=f't')
        axs[1,1].set(xlabel=f't')

    fig.savefig('sl.7.14.pdf')
    fig.show()

# program_7_8.py
'''
   Rješavanje sustava Lorenzovih diferencijalnih jednadžbi
      dx/dt = a*(y - x)
      dy/dt = x*(b - z) - y
      dz/dt = x*y - c*z
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

t_0 = 0; t_f = 10.; m = 500
te = np.linspace(t_0,t_f,m)

# Preimenivanje varijabli: x = x1, y = x2, z = x3
def Lorenz(t,x,a,b,c):
    x1,x2,x3 = x
    dx1dt = -a*x1 + a*x2
    dx2dt = b*x1 - x2 -     x1*x3
    dx3dt = x1*x2 - c*x3
    return [dx1dt, dx2dt, dx3dt]

if __name__ == '__main__':
    fig,axs = plt.subplots(2,2,figsize=(8,6),layout='constrained')
# Koeficijenti jednadžbi
    a = 10; b = 28; c = 8/3
# Početne vrijednsti x(0)=x1_0, y(0)=x2_0, z(0)=x3_0
    x1_0 = 10.0; x3_0 = 10.0
    x2_0 = 0.999998
    for i in range(4):
        x2_0 += 0.000002
        sol = solve_ivp(Lorenz,[0,t_f],[x1_0,x2_0,x3_0],method='LSODA',
                        t_eval=te,args=(a,b,c))
        r,s = divmod(i,2)
# Rješenja za sve tri varijable x(t),y(t),z(t)       
        x = sol.y[0, : ]; y = sol.y[1, : ]; z = sol.y[2, : ]
# Grafički prikaz rješenja varijable x(t)
        axs[r,s].set(title=f'Rješenje x(t) Lorenzova sustava uz'+'\n'+
                        f'x(0)={x1_0}, y(0)={x2_0:7.6f}, z(0)={x3_0}')
        axs[r,s].plot(te,x,lw=1.0)
        axs[0,0].set(ylabel=f'x(t)')
        axs[1,0].set(ylabel=f'x(t)')
        axs[1,0].set(xlabel=f't')
        axs[1,1].set(xlabel=r't')

    fig.savefig('sl.7.13.pdf')
    fig.show()

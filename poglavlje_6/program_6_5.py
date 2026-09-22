# program_6_5.py
'''
    Rješenje diferencijalne jednadžbe
        dx(t)/dt = -0.25*x(t) + r(t)
        r(t) = np.cos(3*t)
    uz početni uvjet x[0] = -1.
'''
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t_0 = 0.;  t_f = 15.
    x_0 = -1.
    te = np.linspace(t_0,t_f,1001)

    def r(t):
        return np.cos(3*t)

    def jedn(t,x):
        x = -0.25*x + r(t)
        return x

    fig,ax = plt.subplots()
    
    sol = solve_ivp(jedn,[t_0,t_f],[x_0],method='LSODA',dense_output=True)
    ax.set(title='Rješenje jednadžbe s nezavisnom vremenskom funkcijom',
           xlabel='t', ylabel='x(t),r(t)')
    ax.plot(sol.t,sol.y[0, : ],lw=1.0,label='x(t)')
    ax.plot(te,r(te),lw=1.0,label='r(t)')
    ax.legend(loc='upper left')

    fig.savefig('sl.6.14.pdf')
    fig.show()

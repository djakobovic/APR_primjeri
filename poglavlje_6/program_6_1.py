# program_6_1.py
'''
Eulerovim postupkom odrediti numeričko rješenje diferencijalne jednadžbe
    dx(t)/dt = 0.8*t+0.1
u intervalu
    [t_0,t_f] = [1,10]
uz početno stanje
    x(t_0)= 1
i usporediti ga s poznatim analitičkim rješenjem
    x(t)= 0.4*t**2+0.1*t+1
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext',fontset='stix')

'''
Definicija funkcije i pripadne diferencijalne jednadžbe
'''
def fun(a,b,c,t):
    return a*t**2+b*t+c

def der_fun(a,b,t):
    return 2*a*t+b


if __name__ == '__main__':
    t_0 = 0.; t_f = 10.
    a = 0.4; b = 0.1; c = 1
    x_0 = c
    '''
       Priprema koordinatnih osi
    '''
    fig,axs = plt.subplots(2,1,figsize=(4,5),layout='constrained')
    t_gr = (t_0,t_f)
    x_gr = (0,fun(a,b,c,t_f))
    axs[0].set(title=r'Grafički prikaz funkcije'+'\n'+r'$x=0.4t^2+0.1t+1$',
            ylabel='x(t)')        
    axs[1].set(title=r'Rješenja diferencijalne jednadžbe'+'\n'+r'$dx/dt=0.8t+0.1$',
           xlabel=r't',ylabel='x(t)')
    for i in range(2):
        axs[i].set(xlim=t_gr,ylim=x_gr,xticks=[],yticks=[])
        axs[i].set_xticks([0,1,2,3,4,5,6,7,8,9,10],
                           [r'0',r'1',r'2',r'3',r'4',r'5',r'6',r'7',r'8',r'9',r'10'])
        axs[i].set_yticks([0,5,10,15,20,25,30,35,40],
                          [r'0',r'5',r'10',r'15',r'20',r'25',r'30',r'35',r'40'])
        axs[i].grid(axis='both',c='gray',ls=':',lw=0.5)

    '''
       Crtanje funkcije
    '''
    t = np.linspace(t_0,t_f,101)
    axs[0].plot(t,fun(a,b,c,t),lw=0.7)
    '''
       Crtanje rješenja diferencijalne jednadžbe Eulerovim postupkom
       uz različite veličine koraka T
    '''
    x_0 = c
    n = np.array([3,6,11,21,101])
    for j in range(5):
        T = (t_f - t_0)/(n[j]-1)
        t = np.linspace(t_0,t_f,n[j])
        x_t = np.zeros(n[j])
        x_t[0] = x_0
        for k in range(n[j]-1):
            x_t[k+1] = x_t[k] + T*der_fun(a,b,t[k])
        axs[1].plot(t,x_t,lw=0.7,label=T)
    axs[1].legend(loc='upper left',title=r'$T$')

    fig.show()
    fig.savefig('sl.6.4.pdf')

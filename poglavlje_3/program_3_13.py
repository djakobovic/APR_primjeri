# program_3_13.py
'''
Crtanje grafa funkcije f(x) = 3+x/((x - 2)(x + 1))
u intervalu [-5,5] uz
    x = np.linspace(-5,5,1000)
    x = np.linspace(-5,5,1001)  
'''
import numpy as np
import matplotlib.pyplot as plt

x_0 = np.linspace(-5, 5, 1000)
y_0 = 3 + x_0/((x_0 - 2)*(x_0 +1))
x_1 = np.linspace(-5, 5, 1001)
y_1 = 3 + x_1/((x_1 - 2)*(x_1 +1))

fig,axs = plt.subplots(1,2,figsize=(9,4),sharey=True,
                       layout='constrained')

def graf(x, y, i):
    axs[i].set(xlim=(-5,5),ylim=(0,5),xlabel='x',
               title='y = 3 + x/((x-2)*(x+1))')
    if i == 0:
        axs[i].set_ylabel('y')
    axs[i].plot(x,y,'k-',lw=1.0)
    tekst = ('linspace(-5,5,1000)','linspace(-5,5,1001)')
    axs[i].text(-4.8, 4, tekst[i], color='k', fontsize=11)

if __name__ == '__main__':
    graf(x_0,y_0,0)
    graf(x_1,y_1,1)
   
    fig.savefig('sl.3.16.pdf')
    fig.show()

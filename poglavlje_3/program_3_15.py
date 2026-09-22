# program_3_15.py
'''
Maskiranje poredaka
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,51)
y = np.sin(x)

fig,axs = plt.subplots(2,2,layout='constrained',
                       sharex=True,sharey=True)

if __name__ == '__main__':
    axs[0,0].set(ylabel='y',xlim=(-np.pi,np.pi),ylim=(-1.5,1.5))
    axs[0,0].plot(x,np.ma.masked_less(y,0.5),'k-',lw=1.0)
    axs[0,0].text(-2.0,-1.25,'masked_less(y,0.5)',fontsize=10)
                  
    axs[0,1].set(xlim=(-np.pi,np.pi),ylim=(-1.5,1.5))
    axs[0,1].plot(x,np.ma.masked_greater(y,0.5),'k-',lw=1.0)
    axs[0,1].text(-2.0,-1.35,'masked_greater(y,0.5)',fontsize=10)
                  
    axs[1,0].set(xlabel='x', ylabel='y',
                 xlim=(-np.pi,np.pi),ylim=(-1.5,1.5))
    axs[1,0].plot(x,np.ma.masked_inside(y,-0.5,0.5),'k-',lw=1.0)
    axs[1,0].text(-2.5,-1.35, 'masked_inside(y,-0.5,0.5)',fontsize=10)
    
    axs[1,1].set(xlabel='x',xlim=(-np.pi,np.pi),ylim=(-1.5,1.5))
    axs[1,1].plot(x,np.ma.masked_outside(y,-0.5,0.5),'k-',lw=1.0)
    axs[1,1].text(-2.5,-1.35,'masked_outside(y,-0.5,0.5)',fontsize=10) 

    fig.savefig('sl.3.17.pdf')
    fig.show()

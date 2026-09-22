# program_4_24.py
'''
Razmještaj brojeva u kompleksnoj ravnini s kartezijevim i
polarnim koordinatama
'''
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(5,5))

def kompl_ravnina(naziv):
    ax.set(title=naziv, xlabel='x', ylabel='yj',
           xlim=(-10,10),ylim=(-10,10),aspect='equal',
           xticks = np.arange(-10,11,2), yticks = np.arange(-10,11,2))    
    ax.grid(axis='both', c='gray', ls=':', lw=0.5)
    ax.plot(0,0,'o',ms=4)
    ax.text(0.2,-0.20,'0+0j',ha='left',va='top',fontsize=10)

def kompl_broj(x,y):
    ax.plot(x,y,'o',ms=3)
    '''
    U svakom kvadrantu broj se ispisuje s vanjske strane.
    '''
    if y <0:
        if x < 0:
            ax.text(x,y,f'{x}+{y}j',ha='right',va='top',fontsize=10)
        else:
            ax.text(x,y,f'{x}+{y}j',ha='left',va='top',fontsize=10)            
    else:
        if x < 0:
            ax.text(x,y,f'{x}+{y}j',ha='right',va='bottom',fontsize=10)
        else:
            ax.text(x,y,f'{x}+{y}j',ha='left',va='bottom',fontsize=10)            
    '''
    Crtanje radij vektora
    '''
    x_p = np.array([0,x])
    y_p = np.array([0,y]) 
    ax.plot(x_p,y_p,'k',lw=0.7)
    '''
    Luk kuta crta se s polumjerom 0.3 udaljenosti od točke ishodišta
    '''
    d = 0.3*np.sqrt(x**2+y**2)
    fi = np.arctan2(y,x)
    fi_p = np.linspace(0,fi)
    x = d*np.cos(fi_p)
    y = d*np.sin(fi_p)
    ax.plot(x,y,'k',lw=0.5)             

if __name__ == '__main__':
    naziv ='Kompleksna ravnina'
    kompl_ravnina(naziv)
    kompl_broj(7,0)
    ax.text(4.0,-1.2, f'r = {np.abs(7+0j):4.2f}', ha='left',va='top')    
    ax.text(4.0,-0.2,r'$\varphi$ ='+f'{np.angle(7+0j):4.2f}', ha='left',va='top')  
    kompl_broj(8,6)
    ax.text(5.7,3.9,f'r = {np.abs(8+6j):4.2f}', ha='left',va='top')
    ax.text(3.1,1.0,r'$\varphi$ ='+f'{np.angle(8+6j):4.2f}', ha='left',va='center')
    kompl_broj(-4,6)
    ax.text(-2.8,4.5,f'r = {np.abs(-4+6j):4.2f}', ha='left',va='bottom')
    ax.text(0.5,2.2,r'$\varphi$ ='+f'{np.angle(-4+6j):4.2f}', ha='center',va='bottom')
    kompl_broj(-6,0)
    ax.text(-4.8,-0.2, f'r = {np.abs(-6+0j):4.2f}', ha='left',va='top')    
    ax.text(-1.9,0.5,r'$\varphi$ ='+f'{np.angle(-6+0j):4.2f}', ha='right',va='bottom')  
    kompl_broj(-7,-5)
    ax.text(-5.0,-3.8, f'r = {np.abs(-7-5j):4.2f}', ha='left',va='top')
    ax.text(1.0,-3.5,r'$\varphi$ ='+f'{np.angle(-7-5j):4.2f}', ha='center',va='bottom')
  
    fig.savefig('sl.7.pdf')
    fig.show()
    

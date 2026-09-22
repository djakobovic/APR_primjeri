# program_3_20.py
'''
Crtanje kontura funkcije f = x_1**2+x_2**2 - 2 odabranim vrijednostima
razina s eksplicitno definiranim stilom linija, zadanim razinama i odabranim
lokacijama ispisa vrijednosti razina te oznacenom tockom minimuma f=-2.
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rc('mathtext',fontset='stix')

x_0 = np.linspace(-2,2,201)
x_1 = np.linspace(-2,2,201)
X_0,X_1 = np.meshgrid(x_0,x_1)
F = X_0**2+X_1**2 - 2
razine = np.array([-1.85, -1.5, -1, 0, 1, 2, 3])
lokacije = [(-0.20,0.10),(-0.5,0.5),(-0.75,0.75),(-1.0,1.0),
            (-1.3,1.3),(-1.4,1.4),(-1.65,1.65) ]

fig,ax=plt.subplots()

if __name__ == '__main__':   
    ax.set(aspect='equal')
    ax.set_title('Vrijednosti kontura ispisane na odabranim mjestima',fontsize=10)
    ax.set_xlabel(r'$x_0$',fontsize=12)
    ax.set_ylabel(r'$x_1$',fontsize=12)
    ax.set_xticks(np.linspace(-2,2,9))
    ax.set_yticks(np.linspace(-2,2,9))                  
    ax.grid(axis='both',color='gray',ls=':',lw=0.5)

    ax.axvline(c='gray',lw=1.0); ax.axhline(c='gray',lw=1.0)    
    kontura=ax.contour(X_0,X_1,F,levels=razine,colors='k',linewidths=0.5,
                        linestyles='-')
    ax.clabel(kontura,inline=True,fontsize=8,manual=lokacije)
    ax.plot(0,'ko',ms=3)
    ax.text(0.01,0.04,'-2.00',fontsize=8)

    fig.savefig('sl.3.22.pdf')
    fig.show()


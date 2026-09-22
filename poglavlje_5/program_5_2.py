# program_5_2.py
'''
Valni oblici napona i struja kroz impedancije Z1 i Z2.
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rc('mathtext',fontset='stix')

def graf_prikaz():
    x_gr = (-7,7)
    y_gr= (-12,12)
    ax.set(xlim=x_gr,ylim=y_gr,xticks=[],yticks=[])
    ax.set(title=naziv,xlim=x_gr,ylim=y_gr)       
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['bottom']].set_position('center')
    ax.spines[['left']].set_position('center')
    ax.set_xticks([-2*np.pi,-3/2*np.pi,-np.pi,-np.pi/2,np.pi/2,np.pi,3/2*np.pi,2*np.pi],
                  [r'$-2\pi$',r'$-\frac{3}{2}\pi$',r'$-\pi$',r'$-\frac{1}{2}\pi$',
                   r'$\frac{1}{2}\pi$',
                   r'$\pi$',r'$\frac{3}{2}\pi$',r'$2\pi$'])
    ax.set_yticks([-10,-8,-6,-4,-2,2,4,6,8,10],
                  [r'$-10$',r'$-8$',r'$-6$',r'$-4$',r'$-2$',
                   r'$2$',r'$4$',r'$6$',r'$8$',r'$10$'])
    for i in range(9):
        ax.axvline(x = -2*np.pi + i*np.pi/2, c='k',ls='--',lw=0.4)

if __name__ == '__main__':
    naziv = 'Valni oblici napona\n i struja kroz impedancije Z1 i Z2'
    U = 10
    R = 1.25
    L = 2*10**-3
    C = 0.25*10**-3
    omega = 10**3
    print(f'U = {U} V\nR = {R} ohm\nL = {L} henri\nC = {C} farad')
    print(f'omega = {omega} radian/s')
     
    Z_1 = R + (omega*L)*1j
    Z_2 = R - (1/(omega*C))*1j
    print(f'\nZ_1 = {Z_1}\nZ_2 = {Z_2}')
    I_1 = U/np.abs(Z_1); theta_1 = np.angle(U)-np.angle(Z_1)
    I_2 = U/np.abs(Z_2); theta_2 = np.angle(U)-np.angle(Z_2)
    print(f'I_1 = {I_1}  theta_1 = {theta_1}')
    print(f'I_2 = {I_2}  theta_2 = {theta_2}')    

    fig,ax = plt.subplots()
    x = np.linspace(-2*np.pi,2*np.pi,num=100)   
    u = U*np.cos(x)
    i_1 = I_1*np.cos(x + theta_1)
    i_2 = I_2*np.cos(x + theta_2)
                        
    graf_prikaz()
    ax.plot(x,u,'k-',lw=1.0, label=r'$u(t)=Ucos(\omega$'+r'$t)$')
    ax.plot(x,i_1,'b--',lw=1.2, label=r'$i_1(t)$')
    ax.plot(x,i_2,'r-.',lw=1.2, label=r'$i_2(t)$')
    ax.legend(loc='upper right',title='napon i struje')    

    fig.savefig('sl.5.9.pdf')
    fig.show()
    

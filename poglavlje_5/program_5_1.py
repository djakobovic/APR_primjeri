# program_5_1.py
'''
Valni oblici napona i struja kroz otpornik R, induktivitet L i kapacitet C
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
    naziv = 'Valni oblici napona\n i struja kroz otpornik R, induktivitet L i kapacitet C'
    U = 10
    R = 1.25
    L = 2*10**-3
    C = 0.25*10**-3
    omega = 10**3
    print(f'U = {U} V\nR = {R} ohm\nL = {L} henri\nC = {C} farad')
    print(f'omega = {omega} radian/s')
     
    Z_R = R + 0j
    Z_L = 0 + (omega*L)*1j
    Z_C = 0 - (1/(omega*C))*1j
    print(f'\nZ_R = {Z_R}\nZ_L = {Z_L}\nZ_C = {Z_C}')
    I_R = U/np.abs(Z_R); theta_R = np.angle(U)-np.angle(Z_R)
    I_L = U/np.abs(Z_L); theta_L = -np.angle(Z_L)
    I_C = U/np.abs(Z_C); theta_C = -np.angle(Z_C)
    print(f'i_R ima fazor: I_R = {I_R}  theta_R = {theta_R}')
    print(f'i_L ima fazor: I_L = {I_L}  theta_L = {theta_L}')    
    print(f'i_C ima fazor: I_C = {I_C}  theta_C = {theta_C}')

    x = np.linspace(-2*np.pi,2*np.pi,num=100)
    fig,ax = plt.subplots()
    u = U*np.cos(x)
    i_R = I_R*np.cos(x + theta_R)
    i_L = I_L*np.cos(x + theta_L)
    i_C = I_C*np.cos(x + theta_C)
                        
    graf_prikaz()
    ax.plot(x,u,'k-',lw=1.0, label=r'$u(t)=Ucos(\omega$'+r'$t)$')
    ax.plot(x,i_R,'k:', lw=1.2, label=r'$i_R(t)$')
    ax.plot(x,i_L,'b--',lw=1.2, label=r'$i_L(t)$')
    ax.plot(x,i_C,'r-.',lw=1.2, label=r'$i_C(t)$')
    ax.legend(loc='upper right',title='napon i struje')    

    fig.savefig('sl.5.7.pdf')
    fig.show()

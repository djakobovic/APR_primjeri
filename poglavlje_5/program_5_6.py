# program_5_6.py
'''
Amplitude karakteristike udvostručenog i utrostručenog
RC filtra dobivene matričnim rješenjem njihovih sklopova
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sla
plt.rc('mathtext',fontset='stix')

def rješenje_2(omg,R,C,U):
    '''
    Funkcija za rješavanje udvostručenog RC filtra
    s oznakama koje proizlaze iz slike 5.17.a)
    '''
    Z_0 = Z_2 = R + 0j;    Z_1 = Z_3 = -1j/(omg*C)
    A = np.zeros((4,4),dtype=complex)
    A[0,0] = Z_0; A[0,1] = Z_1
    A[1,0] = 0 ; A[1,1] = -Z_1; A[1,3] = Z_3
    A[2,0] = 1;  A[2,1] = -1;    A[2,2] = -1
    A[3,2] = 1;  A[3,3] = -1
    b = np.zeros((4,1), dtype=complex)
    b[0] = U                 
    I = sla.solve(A,b)
    '''
    Izlazni napon određen je padom napona određenog
    strujom I[3] na impedanciji Z_3.
    '''    
    return np.abs(I[3]*Z_3)[0]

def rješenje_3(omg,R,C,U):
    '''
    Funkcija za rješavanje utrostručenog RC filtra
    s oznakama koje proizlaze iz slike 5.17.b)
    '''    
    Z_0 = Z_2 = Z_4 = R + 0j
    Z_1 = Z_3 = Z_5 = -1j/(omg*C)
    A = np.zeros((6,6),dtype=complex)
    A[0,0] = Z_0;  A[0,1] = Z_1
    A[1,1] = -Z_1; A[1,2] = Z_2; A[1,3] = Z_3
    A[2,3] = -Z_3; A[2,4] = Z_4; A[2,5] = Z_5
    A[3,0] = 1;    A[3,1] = -1;  A[3,3] = -1
    A[4,2] = 1;    A[4,3] = -1;  A[4,4] = -1
    A[5,4] = 1;    A[5,5] = -1
    b = np.zeros((6,1), dtype=complex)
    b[0] = U   
    I = sla.solve(A,b)
    '''
    Izlazni napon određen je padom napona određenog
    strujom I[5] na impedanciji Z_5.
    '''
    return np.abs(I[5]*Z_5)[0]

if __name__ == '__main__':
    R = 10**3 
    C = 10**-6
    U = 1     
    omega = np.arange(10**1,10**5,1)

    fig,ax = plt.subplots()

    ax.set(title=r'$RC$'+' '+r'$filtri$',
           xlabel=r'$kutna$'+' '+r'$frekvencija$'+' '+r'$\omega$',
           ylabel=r'$amplituda$') 

    U_iz = np.zeros(len(omega))
    for i in range(len(omega)):
        U_iz[i] = rješenje_2(omega[i],R,C,U)
    ax.semilogx(omega,U_iz,lw=1.0,label='udvostručeni RC filtar')
    U_iz = np.zeros(len(omega))
    for i in range(len(omega)):
        U_iz[i] = rješenje_3(omega[i],R,C,U)
    ax.semilogx(omega,U_iz,lw=1.0,label='utrostručeni RC filtar')
 
    ax.grid()
    ax.legend(loc='lower left')
    ax.axhline(y = 0.707, ls='--',lw = 1.2)
    ax.text(10**1,0.65,r'$0.707$')

    fig.savefig('sl.5.18.pdf')
    fig.show()

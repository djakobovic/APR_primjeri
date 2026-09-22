# program_4_5.py
'''
Vizualizacija funkcija koje određuju složenost
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rc('mathtext', fontset='stix')

n = np.arange(101)
m = np.arange(25)
m_fakt = np.zeros(25)
m_fakt[0] = 1; m_fakt[1] = 1
for i in range(2,25):
    m_fakt[i] = m_fakt[i-1] + m_fakt[i-2]

if __name__ == '__main__':
    fig,(ax0,ax1) = plt.subplots(1,2,figsize=(6,3),layout='constrained')

    ax0.set_title(r'$f(n):   log(n),    n,   nlog(n),   n^2$',fontsize=12)
    ax0.set(xlabel=r'$n$', ylabel=r'$f(n)$', xlim=(0,100),ylim=(0,100))
    ax0.plot(n,np.log(n),'k:',lw=0.8, label=r'$log(n)$')
    ax0.plot(n,n*np.log(n),'k--',lw=0.8, label=r'$nlog(n)$')
    ax0.plot(n,n,'k-.',lw=0.8,label=r'$n$')
    ax0.plot(n,n**2,'k-',lw=1.5, label=r'$n^2$')
    ax0.legend(loc='lower right', title=r'$f(n)$')    

    ax1.set_title(r'$f(n):  n^2,   n^3,   n!,   2^n$', fontsize=12)
    ax1.set(xlabel=r'$n$', ylabel=r'$f(n)$',
           xlim=(0,25),ylim=(0,10000))
    ax1.plot(n,n**2,'k-',lw=1.5, label=r'$n^2$')
    ax1.plot(m,m**3,'k--',lw=0.8, label=r'$n^3$')
    ax1.plot(m, m_fakt,'k-.',lw=0.8, label=r'$n!$')
    ax1.plot(m,2**m,'k:',lw=0.8, label=r'$2^n$')
    ax1.legend(loc='best', title=r'$f(n)$')   

    fig.savefig('sl.4.4.pdf')
    fig.show()

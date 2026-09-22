# program_3_10.py
'''
Program u ravnini omeđenoj s xlim=(0,10), ylim=(0,10)
ispisuje koordinate u razlicitim položajima i razlicitim velicinama fonta
'''
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

if __name__ == '__main__':
    naziv = f'Opisi koordinata smješteni na više načina\ni s različitim veličinama znakova' 
    ax.set(title=naziv,xlim=(0,10),ylim=(0,10),
           xticks=np.arange(11),yticks=np.arange(11))
    ax.grid(axis='both', c='gray', ls=':', lw=0.5)
    ax.plot(1,8,'o',ms=2);ax.text(1,8,'(1,8)',ha='left',va='bottom',fontsize=20)
    ax.plot(5,8,'o',ms=2);ax.text(5,8,'(5,8)',ha='center',va='bottom',fontsize=18)
    ax.plot(9,8,'o',ms=2);ax.text(9,8,'(9,8)',ha='right',va='bottom',fontsize=16)
    ax.plot(1,5,'o',ms=2);ax.text(1,5,'(1,5)',ha='left',va='center',fontsize=14)
    ax.plot(5,5,'o',ms=2);ax.text(5,5,'(5,5)',ha='center',va='center',fontsize=12)
    ax.plot(9,5,'o',ms=2);ax.text(9,5,'(9,5)',ha='right',va='center',fontsize=10)
    ax.plot(1,2,'o',ms=2);ax.text(1,2,'(1,6)',ha='left',va='top',fontsize=8)
    ax.plot(5,2,'o',ms=2);ax.text(5,2,'(5,2)',ha='center',va='top',fontsize=6)
    ax.plot(9,2,'o',ms=2);ax.text(9,2,'(9,2)',ha='right',va='top',fontsize=4)

    fig.savefig('sl.3.13.pdf')
    fig.show()

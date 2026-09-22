# program_4_11.py
'''
Eksponent kvocijenta dvaju brojeva x i y
jednkak je ed = edx - edy
'''
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig,ax = plt.subplots()

    ax.set(title='Eksponent kvocijenta edx-edy', xlabel='edx', ylabel='edy',
            xlim=(-6,6),ylim=(-6,6),aspect='equal',
            xticks = np.arange(-5,6), yticks = np.arange(-5,6))    
    ax.grid(axis='both', c='gray', ls=':', lw=0.5)  
    for i in range(-5,6):
        for j in range(-5,6):
            ax.text(i,j,str(i-j),ha='center',va='center',fontsize=10)

    fig.savefig('sl.4.5.pdf')
    fig.show()

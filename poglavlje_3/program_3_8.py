# program_3_8.py
'''
Crtanje koordinatnog sustava
'''
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig,ax = plt.subplots(figsize=(5,5))
    ax.set(title='Koordinatni sustav', xlabel='x', ylabel='y',
           xlim=(-10,10),ylim=(-10,10),aspect='equal',
           xticks = np.arange(-10,11,2), yticks = np.arange(-10,11,2))    
    ax.grid(axis='both', c='gray', ls=':', lw=0.5)       

    fig.savefig('sl.3.11.pdf')
    fig.show()

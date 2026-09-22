# program_3_2.py
'''
Slika s više crteža
'''
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig,((ax0,ax1),(ax2,ax3)) = plt.subplots(2,2)
         
    ax0.set_title('Crtež 0')
    ax0.set_xlabel('x')    
    ax0.set_ylabel('y')
         
    ax1.set_title('Crtež 1')
    ax1.set_xlabel('x')    
    ax1.set_ylabel('y')
         
    ax2.set_title('Crtež 2')
    ax2.set_xlabel('x')    
    ax2.set_ylabel('y')
         
    ax3.set_title('Crtež 3')
    ax3.set_xlabel('x')    
    ax3.set_ylabel('y')
         
    fig.savefig('sl.3.5.pdf')
    fig.show()                          



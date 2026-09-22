# program_3_1.py
'''
Najjednostavniji prikaz funkcije sin(x)
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)

if __name__ == '__main__':
    plt.plot(x, np.sin(x))                  
    plt.xlabel('x[rad]')                    
    plt.ylabel('sin(x)')

    plt.savefig('sl.3.2.pdf')  
    plt.show()                          

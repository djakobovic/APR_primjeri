# program_2_10.py
'''
Primjer ispisa vrijednosti funkcije
'''
import numpy as np

if __name__ == '__main__':
    x = np.linspace(-np.pi,np.pi,21)
    y = np.sin(x)
    np.set_printoptions(3)
    print(f'x =\n{x}')
    print(f'sin(x) =\n{y}')
    y[0] = y[20] = 0.     
    print(f'sin(x) =\n{y}')    

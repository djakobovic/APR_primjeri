# program_2_9.py
'''
Primjeri uporabe univerzalnih funkcija
'''
import numpy as np

w = np.linspace(0,np.pi,5)
x = np.linspace(0,5,6)
y = np.logspace(0,5,6)
z = np.logspace(0,5,6,base=np.e)

if __name__ == '__main__':
    np.set_printoptions(3)
    print(f'w = {w}')
    print(f'sin(w)        =  {np.sin(w)}')
    print(f'cos(w)        = {np.cos(w)}')
    print(f'tan(w)        = {np.tan(w)}')
    print(f'sin(w)/cos(w) = {np.sin(w)/np.cos(w)}\n')
    print(f'x = {x}')
    print(f'exp(x) = {np.exp(x)}\n')
    print(f'y = {y}') 
    print(f'log10(y) = {np.log10(y)}\n')
    print(f'z = {z}')
    print(f'log(z) = {np.log(z)}')

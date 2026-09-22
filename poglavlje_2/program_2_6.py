# program_2_6.py
'''
Problemi s poredcima velikh brojeva
'''
import numpy as np

h = [10**6,10**6+1,10**6+2]
k = np.array(h, dtype = 'int32')

if __name__ == '__main__':
    print(f'lista h      = {h}')
    print(f'poredak k    = {k}')
    for i in range(len(h)):
        h[i] = h[i]**2
        k[i] = k[i]**2
    print(f'lista h**2   = {h}')
    print(f'poredak k**2 = {k}')

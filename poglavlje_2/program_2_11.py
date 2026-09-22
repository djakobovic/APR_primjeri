# program_2_11.py
'''
Aritmetičke operacije s 2D-poredcima
'''
import numpy as np

A = np.random.randint(5,size=(3,3))
B = np.random.randint(10,size=(3,3))

if __name__ == '__main__':
    print(f'A =\n{A}')
    print(f'B =\n{B}')
    print(f'A + B =\n{A + B}')
    print(f'A - B =\n{A - B}')
    print(f'A * B =\n{A * B}')
    print(f'A / B =\n{A / B}')

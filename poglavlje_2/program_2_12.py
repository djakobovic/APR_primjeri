# program_2_12.py
'''
Aritmeticke operacije skalara s 2D-poretkom
'''
import numpy as np

A = np.random.randint(10,size=(3,3))
v = np.random.randint(2,4)

print(f'v = {v}')
print(f'A =\n{A}')

print(f'v + A =\n{v + A}')
print(f'v * A =\n{v * A}')
print(f'A**v =\n{A**v}')

# program_2_8.py
'''
Aritmetičke operacije skalara s poretkom
'''
import numpy as np

a = np.arange(0,10,2)
b = np.arange(1,11,2)
x = 2
y = 5

if __name__ == '__main__':
    print(f'a = {a}   b = {b}')
    print(f'x = {x}   y = {y}')
    print(f'a/x = {a/x}')
    print(f'a * x = {a*x}')
    print(f'a/y  = {a/y}')
    print(f'y/b = {y/b}')
    print(f'x**a = {x**a}')
    print(f'y**b = {y**b}')
    print(f'x*a + y*b = {x*a +y*b}')
    print(f'(y*b)/(x*a) = {(y*b)/(x*a)}')

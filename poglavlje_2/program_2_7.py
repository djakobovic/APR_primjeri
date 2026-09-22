# program_2_7.py
'''
Aritmetičke operacije s poredcima
'''
import numpy as np

a = np.arange(0,10,2)
b = np.arange(1,11,2)

if __name__ == '__main__':
    print(f'a = {a}\nb = {b}')
    print(f'a + b = {a + b}')
    print(f'a - b = {a - b}')
    print(f'b - a = {b - a}')
    print(f'a * b = {a * b}')
    print(f'a / b = {a / b}')
    print(f'b / a = {b / a}')
    print(f'a**2 + b**2 = {a**2 + b**2}')
    print(f'b**a = {b**a}')

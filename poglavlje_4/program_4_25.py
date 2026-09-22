# program_4_25.py
'''
Operacije s kompleksnim vektorima
'''
import numpy as np
import scipy.linalg as sla

if __name__ == '__main__':
    z_1 = np.array([[0],[1+1j],[1j],[-1+1j],[-1],[-1-1j],[-1j],[1-1j]])
    z_2 = np.array([[0],[1],[2],[3],[4],[5],[6],[7]], dtype=complex)
    print(f'z_1.T = {z_1.T}')
    print(f'z_2.T = {z_2.T}')    
    print(f'z_1.real.T = {z_1.real.T}')
    print(f'z_1.imag.T = {z_1.imag.T}')
    print(f'z_2.real.T = {z_2.real.T}')
    print(f'z_2.imag.T = {z_2.imag.T}')
    np.set_printoptions(3)
    print(f'\nnp.abs(z_1).T =    {np.abs(z_1).T}')
    print(f'np.angle(z_1).T = {np.angle(z_1).T}')
    print(f'np.angle(z_1,deg=True).T = {np.angle(z_1,deg=True).T}')

    print(f'\n(z_1 + z_2).T = {(z_1 + z_2).T}')
    print(f'z_1.T @ z_2  = {z_1.T @ z_2}')

# program_4_26.py
'''
Operacije s kompleksnim matricama 
'''
import numpy as np
import scipy.linalg as sla
from numpy.linalg import cond as kond

np.set_printoptions(3)
N = np.zeros((3,3),dtype=complex)
J = np.ones((3,3),dtype=complex)
I = np.identity(3,dtype=complex)
A = np.array([[1,1j,1+1j],[4j,5j,6j],[1+7j,2+8j,3+9j]])
B = np.array([[3,2,1],[4,3,2],[3,5,7]],dtype=complex)

if __name__ == '__main__':
    print(f'N = np.zeros((3,3),dtype=complex) =\n{N}')
    print(f'J = np.ones((3,3),dtype=complex) =\n{J}')
    print(f'I = np.identity(3,3),dtype=complex) =\n{I}')

    print(f'\nA =\n{A}     kond(A) = {kond(A)}')    
    A_inv = sla.inv(A)
    print(f'sla.inv(A) =\n{A_inv}')
    print(f'A @ A_inv =\n{A @ A_inv}')
    print(f'np.allclose(A @ A_inv, I) = {np.allclose(A @ A_inv, I)}')

    print(f'\nB =\n{B}     kond(B) = {kond(B)}')
    B_inv = sla.inv(B)

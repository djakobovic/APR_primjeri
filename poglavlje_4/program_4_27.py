# program_4_27.py
'''
Rješavanje sustava linearnih jednadžbi Ax = b u kompleksnom području
'''
import numpy as np
import scipy.linalg as sla
from numpy.linalg import cond as kond

A = np.array([[1,1j,1+1j],[4j,5j,6j],[1+7j,2+8j,3+9j]])
b = np.array([[0],[1j],[1+1j]])

if __name__ == '__main__':
    print(f'\nA =\n{A}     kond(A) = {kond(A)}')
    print(f'b.T = {b.T}')
    x = sla.solve(A, b)
    print(f'\nx.T = {x.T}')
    print(f'\nnp.allclose(A @ x, b) = {np.allclose(A @ x, b)}')

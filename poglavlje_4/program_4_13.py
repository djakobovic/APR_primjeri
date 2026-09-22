# program_4_13.py
'''
Razlaganje matrice A na gornju trokutastu matricu U, donju trokutastu matricu L
i permutacijsku matricu P uporabom funkcije lu() modula scipy.linalg
'''
import numpy as np
import scipy.linalg as sla

if __name__ == '__main__':
    A = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]], dtype=float)
    P,L,U = sla.lu(A)
    print(f'A =\n{A}')
    print(f'\nL =\n{L}')
    print(f'U =\n{U}')
    print(f'P =\n{P}')
    print(f'\nP @ L @ U =\n{P @ L @ U}')
    print(f'\nnp.allclose(P @ L @ U, A) = {np.allclose(P @ L @U, A)}')

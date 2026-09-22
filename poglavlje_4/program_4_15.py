# program_4_15.py
'''
Razlaganje matrice A na gornju i donju trokutastu matricu 
uporabom funkcije lu_factor() modula scipy.linalg
'''
import numpy as np
import scipy.linalg as sla

if __name__ == '__main__':
    A = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]], dtype=float)
    print(f'A =\n{A}')
    LU,inp = sla.lu_factor(A)
    print(f'\nLU =\n{LU}')

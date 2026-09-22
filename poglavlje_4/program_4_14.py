# program_4_14.py
'''
Primjer usporedbe dekomponiranih matrica većih dimenzija
'''
import numpy as np
import scipy.linalg as sla

if __name__ == '__main__':
    A = np.random.rand(10,10)
    P,L,U = sla.lu(A)
    print(f'Ispis matrica A i P @ L @ U s tri decimalna mjesta')
    np.set_printoptions(3)
    print(f'A =\n{A}')
    print(f'\nP @ L @ U =\n{P @ L @ U}')
    razlike = 0
    for i in range(10):
        for j in range(10):
            if (P @ L @ U)[i,j] != A[i,j]:
                razlike += 1
    print(f'\nBroj različitih parova u matricama A i P @ L @ U : {razlike}') 
    print(f'\nUsporedba matrica funkcijom np.allclose():')
    print(f'np.allclose(P @ L @ U - A, np.zeros((10,10))) =',end=' ')
    print(f'{np.allclose(P @ L @ U - A, np.zeros((10,10)))}')

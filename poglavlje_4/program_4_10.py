# program_4_10.py
'''
Razlaganje matrice A na donju i gornju trokutastu matricu L i U
'''
import numpy as np

def razlaganje(A):
    (n,n) = A.shape
    L = np.eye(n)

    for k in range(n-1):
        for j in range(k+1,n):
            L[j,k] = A[j,k]/A[k,k]
        for i in range(k+1,n):
            A[i:i+1, : ] = A[i:i+1, : ] - L[i,k]*A[k:k+1, : ]
    return L,A

if __name__ == '__main__':
    A = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]], dtype=float)
    print(f'Matrica A prije poziva funkcije razlaganje(A):\n{A}')
    L,U = razlaganje(A)
    print(f'Matrica A nakon izvodenja funkcije razlaganje(A):\n{A}')          
    print(f'\nL =\n{L}')
    print(f'U =\n{U}')
    print(f'L@U =\n{L@U}')

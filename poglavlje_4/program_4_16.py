# program_4_16.py
'''
Rješavanje sustava Ax = b razlaganjem na matrice L i U,
te postupcima supstitucije unaprijed i supstitucije nazad
'''
import numpy as np
import scipy.linalg as sla

def razlaganje(A):
    '''
    funkcija koja vraća donju trokutastu matricu L i
    gornju trokutastu matricu U bez pivotiranja.
    '''
    (n,n) = A.shape
    U = np.copy(A)
    L = np.eye(n)
    for k in range(n-1):
        for j in range(k+1,n):
            L[j,k] = U[j,k]/U[k,k]
        for i in range(k+1,n):
            U[i:i+1, : ] = U[i:i+1, : ] - L[i,k]*U[k:k+1, : ]
    return L,U

def sup_naprijed(L, b):
    '''
    sup_naprijed(L,b) je funkcija koja vraća rješenje sustava Ly = b
    gdje je L donja trokutasta matrica s jedinicama na dijagonali,
    a b je vektor desne strane jednadžbe 
    '''
    (n,n) = L.shape 
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i][0]
        for j in range(i):
            y[i] -= L[i,j] * y[j]
    return y

def sup_nazad(U, y):
    '''
    sup_nazad(U, y) je funkcija koja vraća rješenje sustava Ux = y
    gdje je U gornja trokutasta matrica, a y je vektor pripadne
    desne strane jednadžbe
    '''
    (n,n) = U.shape
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        pom = y[i]
        for j in range(i+1, n):
            pom -= U[i,j] * x[j]
        x[i] = pom / U[i,i]
    return x

def rješenje(A,b):
    L,U = razlaganje(A)
    y = sup_naprijed(L,b)
    x = sup_nazad(U,y)
    return x

if __name__ == '__main__':
    A = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]], dtype=float)
    b = np.array([[1],[1],[1],[1]])
    x = rješenje(A,b)   
    print(f'A =\n{A}')
    print(f'b.T = {b.T}')
    print(f'x.T = {x.T}')
    print(f'np.allclose(A @ x, b) = {np.allclose(A @ x, b)}')

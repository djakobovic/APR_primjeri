# program_4_20.py
'''
Matrična Frobeniusova norma i euklidska vektorska norma vektora 
dobivenog nadovezivanjem redova matrice
'''
import numpy as np
import scipy.linalg as sla

def frobenius(A):
    (n,n) = A.shape
    x = A.reshape(n**2,1)
    print(f'\nA =\n{A}')
    print(f'sla.norm(A) = {sla.norm(A)}')
    print(f'x.T = {x.T}')
    print(f'sla.norm(x) = {sla.norm(x)}')

if __name__ == '__main__':      
    A_1 = np.array([[20,20,-10,10],[40,41,-20,20],[80,50,-30,40],[3,3,-2,2]])
    A_2 = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]])
    frobenius(A_1)
    frobenius(A_2)

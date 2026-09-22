# program_4_21.py
'''
Utjecaj uvjetovanosti na perturbacije rješenja sustava jednadžbi
promjenama u vektoru b
'''
import numpy as np
import scipy.linalg as sla
from numpy.linalg import cond as kond

def riješi(A, b, bp):
    print(f'\nA =\n{A}')
    kapa = kond(A)
    np.set_printoptions(3)
    print(f'Kondicijski broj kapa = {kapa}')
    x = sla.solve(A,b)
    xp = sla.solve(A,bp)
    print(f'b.T = {b.T} bp.T = {bp.T}  delta_b.T = {(bp - b).T}' )
    print(f'x.T =  {x.T}')
    print(f'xp.T = {xp.T}')
    print(f'delta_x.T = {(xp - x).T}')
    
if __name__== '__main__':
    b = np.array([[1.],[1.],[1.]])
    bp = b + [[0.1],[0],[0]]    
    A = np.array([[1.,2.,3.],[2.,3.,6.],[3.,5.,7.]])
    riješi(A,b,bp)
    A[1,1] = 3.99
    riješi(A,b,bp)
    A[1,1] = 4.0
    riješi(A,b,bp)    

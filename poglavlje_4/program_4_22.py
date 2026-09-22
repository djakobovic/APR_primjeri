# program_4_22.py
'''
Kondicijski broj je beskonačan za singularnu matricu;
Veličina broja blizu singularosti postaje sve veća.
'''
import numpy as np
import scipy.linalg as sla
from numpy.linalg import cond as kond

if __name__== '__main__':
    A = np.array([[1.,2.],[2.,4.]])
    print(f'Za singularnu maticu A =\n{A}')
    print(f's elementima:')
    for i in range(2):
        for j in range(2):
            print(f'A[{i},{j}] = {A[i,j]}',end='  ')
    print(f'\nkondicijski je broj kapa = {kond(A)}')          

    print(f'\nPromjenom elementa A[1,1] pokazuje se da')
    print(f'kondicijski broj raste približavanjem singularnosti')      
    for k in range(7):
        A[1,1] = k * 0.5
        print(f'A[1,1] = {A[1,1]}     kapa = {kond(A)}')
    for k in range(1,11):
        A[1,1] = 3.0 + k*0.1
        print(f'A[1,1] = {A[1,1]}     kapa = {kond(A)}')    

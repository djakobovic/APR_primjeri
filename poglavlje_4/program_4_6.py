# program_4_6.py
'''
Primjeri izracuna determinanti
'''
import numpy as np
import scipy.linalg as sla

A = np.array([1,2,3,4]).reshape(2,2)
B = np.array([2,-1,3,3,1,5,-1,2,-3]).reshape(3,3)
C = np.array([-2,5,0,-1,3,1,-9,0,13,7,3,-1,0,5,-5,
              2,18,0,-7,-10,0,-3,-1,2,3]).reshape(5,5)

if __name__ == '__main__':
    print(f'A =\n{A}\ndet(A) = {sla.det(A)}')
    print(f'\nB =\n{B}\ndet(B) = {sla.det(B)}')
    print(f'\nC =\n{C}\ndet(C) = {sla.det(C)}')

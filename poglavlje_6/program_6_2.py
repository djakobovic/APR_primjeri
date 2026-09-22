# program_6_2.py
'''
Određivanje vektora svojstvenih vrijednosti i
matrice pripadnih svojstvenih vektora M matrice A
'''
import numpy as np
import scipy.linalg as sla
np.set_printoptions(precision=4,suppress=True)

A = np.array([[0.8, 0.3], [0.2, 0.7]])
print(f'Matrica A =\n{A}')

s,M = sla.eig(A)
print(f'\nSvojstvene vrijednosti matrice A =\n{s}')
print(f'\nSvojstveni vektori su stupci matrice M =\n{M}')

D = sla.inv(M) @ A @ M
print(f'\nDijagonalizirana matrica D =\n{D}')

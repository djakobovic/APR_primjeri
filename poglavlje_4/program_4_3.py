# program_4_3.py
'''
Vektori u ravnini
'''
import numpy as np

e0 = np.array([[1],[0]])
e1 = np.array([[0],[1]])
print(f'e0 =\n{e0}')
print(f'e1 =\n{e1}')

def ispis(s0,s1):
    print(f's0 = {s0}   s1 = {s1}')
    u0 = s0*e0
    u1 = s1*e1
    print(f'u0 = s0*e0 =\n{u0}')
    print(f'u1 = s1*e1 =\n{u1}')
    v = u0 + u1
    print(f'v = u0 + u1 = \n{v}')
    print(f'|v| = sqrt((v.T@v)[0,0]) = {np.sqrt((v.T@v)[0,0])}')
    print(f'\nJedinicni vektor u smjeru vektora v je\ne_v = v/|v| =\
\n{v/np.sqrt((v.T@v)[0,0])}')

if __name__=='__main__':
    s0 = 3
    s1 = 4
    ispis(s0,s1)

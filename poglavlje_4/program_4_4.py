# program_4_4.py
'''
Vektori u prostoru
'''
import numpy as np

e0 = np.array([[1],[0],[0]])
e1 = np.array([[0],[1],[0]])
e2 = np.array([[0],[0],[1]])
print(f'e0 =\n{e0}')
print(f'e1 =\n{e1}')
print(f'e2 =\n{e2}')

def ispis(s0,s1,s):
    print(f's0 = {s0}\ns1 = {s1}\ns2 = {s2}')
    u0 = s0*e0
    u1 = s1*e1
    u2 = s2*e2
    print(f'u0 = s0*e0 =\n{u0}')
    print(f'u1 = s1*e1 =\n{u1}')
    print(f'u2 = s2*e2 =\n{u2}')
    v = u0 + u1 + u2
    print(f'v = u0 + u1 + u2 = \n{v}')
    print(f'|v| = sqrt((v.T@v)[0,0]) = {np.sqrt((v.T@v)[0,0])}')
    print(f'\nJedinicni vektor u smjeru vektora v je\ne_v = v/|v| =\
\n{v/np.sqrt((v.T@v)[0,0])}')

if __name__=='__main__':
      s0 = 30
      s1 = 40
      s2 = 50
      ispis(s0,s1,s2)

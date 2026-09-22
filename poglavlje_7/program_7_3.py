# program_7_3.py
'''
   Izračunavanje nultočaka polinoma
       s**n + a_n-2*s**(n-1)+a_n-2*s**(n-2)+...+a_2*s**2+a_1*s+a_0
'''
import numpy as np
import scipy.linalg as sla

if __name__ == '__main__':
    n = int(input('Upisati red polinoma n = '))
    a = np.zeros(n)
    a_upis =input('Upisati koefcijente a_0,a_1,...a_n-1: ').split(',')
    for i in range(n):
        a[i] = float(a_upis[i])
    print(f'a = ', a) 
    A = np.eye(n,k=1)
    for i in range(n):
        A[n-1,i]=-a[i]
    print(f'A =\n{A}')   
    s_nul,M = sla.eig(A)
    for i in range(n):
        print(f's_nul[{i}] = {s_nul[i]:10.3e}')

# program_4_12.py
'''
Razlaganje matrice A na gornju i donju trokutastu matricu
s parcijalnim pivotiranjem
   -  U i L su gornja i donja trokutaste matrice
   -  inp je 1D-poredak u kojem se na mjestu inp[k] upisuje indeks jedadžbe
      u kojoj je pronađen pivot.     
   -  P je permutacijska matrica za rekonstukciju početnog redoslijeda jednadžbi
'''
import numpy as np
import scipy.linalg as sla

def pivotirano_razlaganje(A):
    (n,n) = A.shape
    U = np.copy(A)
    L = np.eye(n)
    inp = np.arange(n,dtype=int)
    P = np.zeros((n,n),dtype=int)
    
    for k in range(n-1):
        # pronalaženje pivota
        pivot = 0.0
        for i in range(k,n):
            if abs(U[i,k] > pivot):
                pivot = abs(U[i,k])
                p = i
        inp[k],inp[p] = inp[p],inp[k]
        # zamjena redoslijeda jednadžbi
        for j in range(n):
            U[k,j],U[p,j] = U[p,j],U[k,j]
        # izračunavanje elementa matrica L i U
        for j in range(k+1,n):
            L[j,k] = U[j,k]/U[k,k]
        for i in range(k+1,n):
            U[i:i+1, : ] = U[i:i+1, : ] - L[i,k]*U[k:k+1, : ]
    #Određivanje permutacijske matrice kojom se vraća početni
    #redoslijed jednadžbi
    for j in range(n):
        P[inp[j],j] = 1
    return L,U,inp,P

if __name__ == '__main__':
    A = np.array([[4,10,11,31],[2,19,10,23],[6,13,5,19],[2,3,1,5]], dtype=float)
    L,U,inp,P = pivotirano_razlaganje(A)
    print(f'A =\n{A}')
    print(f'\nL =\n{L}')
    print(f'U =\n{U}')
    print(f'\ninp = {inp}')
    print(f'P =\n{P}')
    print(f'\nP @ L @ U =\n{P @ L @ U}')

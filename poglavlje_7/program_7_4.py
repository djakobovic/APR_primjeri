# program_7_4.py
'''
Rastav racionalne funkcije
   1/((s-s_0)(s-s_1)...(s-s_i)...(s-s_n-1))
na parcijalne razlomke
    C_0/(s-s_0) + C_1/(s-s_1)+ ...+ C_i/(s-s_i)+...C_n-1/(s-s_n-1)
'''
import numpy as np

n = 4
s_nul = np.array([-2+0j,-3+0j,-2+3j,-2-3j])

if __name__ == '__main__':
    print(f'Uz zadane nultočke nazivnika prijenosne funkcije:')
    for i in range(n):
        print(f'    s_nul[{i}] = {s_nul[i]:10.3e}')
    C = np.zeros(n,dtype=complex)                     
    for i in range(n):
        P = 1.+0j
        for j in range(n):
            if j != i:
                P *= s_nul[j]-s_nul[i]
        C[i] = 1/P 
    print(f'koeficijenti u brojnicima parcijalnih razlomaka su:')
    for i in range(n):
        print(f'    C[{i}] = {C[i]:10.3e}')

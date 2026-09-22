# program_2_5.py
'''
Tolerancija dviju vrijednosti x i y po kriteriju
    abs(x-y)<=atol + rtol*abs(y)
Utvrđuje se gornja granična vrijednost ygr za koji je taj uvijet ispunjen
pri različitim vrijednostima x
'''
import numpy as np

atol = 1e-8
rtol = 1e-5

def tol_i_ygr(x):
    tol = 1.
    ygr = x + tol*x
    while not(abs(x-ygr)<=atol + rtol*abs(ygr)):
        tol = tol/10.
        ygr = x + tol*x
    return tol,ygr

def ispis(x):
    tol, ygr = tol_i_ygr(x)
    print(f' x = {x:12}    tol = {tol:6}    ygr = {ygr:15}')
      
if __name__ == '__main__':
    for i in range(1,11):
        x = 1.*10**(10-i)
        ispis(x)
    for i in range(1,11):
        x = 10**(-i)
        ispis(x)

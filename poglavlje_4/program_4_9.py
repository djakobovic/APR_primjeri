# program_4_9.py
'''
Ispitivanje trajanja računanja
'''
import numpy as np
import scipy.linalg as sla
from timeit import default_timer as sat
                    
if __name__ == '__main__':
    print(f'  n        tk-tp')
    for n in range(20,201,20):
        A = np.random.randint(5, size=(n,n))
        tp = sat()
        d  = sla.det(A)
        tk = sat()
        print(f'{n:>4}    {(tk - tp):12.6e}') 

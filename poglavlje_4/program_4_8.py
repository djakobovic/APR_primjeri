# program_4_8.py
'''
Mjerenje trajanja računanja determinanta 
'''
import numpy as np
import scipy.linalg as sla
from timeit import default_timer as sat
                 
if __name__ == '__main__':
    for n in range(2,5):
        A = np.random.randint(100, size=(n,n))
        print(f'\nn = {n}\nA =\n{A}')
        tp = sat()
        d = sla.det(A)
        tk = sat()
        print(f'd = {d}\ntk-tp = {(tk - tp):12.6e}') 

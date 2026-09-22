
# program_2_13.py
'''
Sortiranje poredaka
'''
import numpy as np

A = np.random.randint(100,size=(3,4))

if __name__ == '__main__':
    print(f'A =\n{A}')
    print(f'np.sort(A) =\n{np.sort(A)}')
    print(f'np.sort(A,axis=0)=\n{np.sort(A,axis=0)}')
    print(f'np.sort(A,axis=None) =\n{np.sort(A,axis=None)}')
    print(f'np.sort(A,axis=None).reshape(3,4) =\n{np.sort(A,axis=None).reshape(3,4)}')
    print(f'np.max(A) = {np.max(A)}')
    print(f'np.min(A) = {np.min(A)}')

    

# program_4_1.py
'''
Operacije s matricama
'''
import numpy as np

def ispis(A,B,C):
    print(f'A =\n{A}')
    print(f'B =\n{B}')
    print(f'C =\n{C}')
    print(f'5*A =\n{5*A}')
    print(f'A+B =\n{A+B}')
    print(f'A@C =\n{A@C}')    

if __name__=='__main__':
    A = np.arange(6).reshape(2,3)
    B = np.arange(6,12).reshape(2,3)
    C = A.reshape(3,2)
    ispis(A,B,C)


    




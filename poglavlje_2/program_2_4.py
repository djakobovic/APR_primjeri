# program_2_4.py
'''
Djelovanje funkcija za usporedbu poredaka
'''
import numpy as np

def ispis(z,ime):
    n = np.size(z)
    print(f'{ime}                     = [ {z[0]}  ',end=' ')
    for i in range(1,n):
        print(f'  {z[i]}  ',end=' ')
    print(f']')    

if __name__ == '__main__':
    x = np.array([1,2,3,4,5,6,7])
    y = np.array([7,6,5,4,3,2,1])
    ispis(x,'x')
    ispis(y,'y')
    print(f'\nnp.equal(x,y)         = {np.equal(x,y)}')
    print(f'x == y                = {x == y}')
    print(f'\nnp.not_equal(x,y)     = {np.not_equal(x,y)}')
    print(f'x != y                = {x != y}')
    print(f'\nnp.greater_equal(x,y) = {np.greater_equal(x,y)}')
    print(f'x >= y                = {x >= y}')
    print(f'\nnp.less_equal(x,y)    = {np.less_equal(x,y)}')
    print(f'x <= y                = {x <= y}')
    print(f'\nnp.greater(x,y)       = {np.greater(x,y)}')
    print(f'x > y                 = {x > y}')
    print(f'\nnp.less(x,y)          = {np.less(x,y)}')
    print(f'x < y                 = {x < y}')

# program_4_2.py
'''
Operacije s vektorima
'''
import numpy as np

def ispis(x,y,r):
    print(f'x=\n{x}')
    print(f'y =\n{y}')
    print(f'x.T ={x.T}')
    print(f'y.T ={y.T}')
    print(f'\nr = {r}')
    print(f'r*x =\n{r*x}')
    print(f'r*y.T = {r*y.T}')
    print(f'\nx.T@y ={x.T@y}')
    print(f'(x.T@y)[0,0] = {(x.T@y)[0,0]}')
    print(f'\nx@y.T =\n{x@y.T}')    

if __name__=='__main__':
    x = np.arange(4).reshape(4,1)
    y = np.arange(4,8).reshape(4,1)
    r = 3
    ispis(x,y,r)

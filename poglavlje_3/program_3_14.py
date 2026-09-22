# program_3_14.py
'''
Istraživanje poredaka x i y = 3 + x/((x-2)*(x+1))
uz x = np.linspace(-5,5) i x = np.linspace(-5,5,1001)
'''
import numpy as np

x_0,dx_0 = np.linspace(-5, 5, 1000, retstep=True)
y_0 = 3 + x_0/((x_0 - 2)*(x_0 +1))
x_1,dx_1 = np.linspace(-5, 5, 1001, retstep=True)
y_1 = 3 + x_1/((x_1 - 2)*(x_1 +1))

np.set_printoptions(3)

if __name__ == '__main__':
    print(f'uz x = np.linspace(-5,5,1000)   korak dx = {dx_0}')
    print(f'- u okolini tocke x = -1')
    print(f'x[398] do x[402]  = {x_0[398:403]}')
    print(f'y[398] do y[402]  = {y_0[398:403]}')
    print(f'- u okolini tocke x = 2')    
    print(f'x[698] do x[702]  = {x_0[698:703]}')
    print(f'y[698] do y[702]  = {y_0[698:703]}')
    print(f'\nuz x = np.linspace(-5,5,1001)   korak dx = {dx_1}')
    print(f' - u okolini tocke x = -1')
    print(f'x[398] do x[402]  = {x_1[398:403]}')
    print(f'y[398] do y[402]  = {y_1[398:403]}')
    print(f'- u okolini tocke x = 2') 
    print(f'x[698] do x[702]  = {x_1[698:703]}')
    print(f'y[698] do y[702]  = {y_1[698:703]}')

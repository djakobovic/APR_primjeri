# program_4_17.py
'''
Primjer rješavanja jednadžbi funkcijom scipy.linalg.solve()
'''
import numpy as np
import scipy.linalg as sla

def rješenje(A,b):
    print(f'\nA =\n{A}\nb.T = {b.T}')
    x = sla.solve(A,b)
    np.set_printoptions(3)
    print(f'\nx.T = {x.T}')
    print(f'np.allclose(A @ x,b) = {np.allclose(A @ x,b)}')    
    
if __name__ == '__main__':
    A_1 = np.array([[20,20,-10,10],[40,41,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_1 = np.array([[40],[60],[120],[60]])
    rješenje(A_1,b_1)
    A_2 = np.random.randint(0,1000,size=(10,10))
    b_2 = np.random.randint(0,1000,size=(10,1))
    rješenje(A_2,b_2)                        

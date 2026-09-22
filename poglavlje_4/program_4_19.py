# program_4_19.py
'''
Primjer rješavanja sustava jednadžbi s matricama koje su blizu singularnosti
'''
import numpy as np
from program_4_17 import rješenje

if __name__ == '__main__':
    A_1 = np.array([[20,20,-10,10],[40,41,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_1 = np.array([[40],[60],[120],[60]])
    rješenje(A_1,b_1)
    A_2 = np.array([[20,20,-10,10],[40,39.99,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_2 = np.array([[40],[60],[120],[60]])
    rješenje(A_2,b_2)
    A_3 = np.array([[20,20,-10,10],[40,40.01,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_3 = np.array([[40],[60],[120],[60]])
    rješenje(A_3,b_3)    

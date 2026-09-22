# program_4_18.py
'''
Pokušaj rješavanja sustava jednadžbi sa singularnom matricom
'''
import numpy as np
import scipy.linalg as sla
from program_4_17 import rješenje

if __name__ == '__main__':
    A_1 = np.array([[20,20,-10,10],[40,41,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_1 = np.array([[40],[60],[120],[60]])
    rješenje(A_1,b_1)
    A_2 = np.array([[20,20,-10,10],[40,40,-20,20],[80,50,-30,40],[3,3,-2,2]])
    b_2 = np.array([[40],[60],[120],[60]])
    rješenje(A_2,b_2)

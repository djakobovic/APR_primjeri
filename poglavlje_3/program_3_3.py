# program_3_3.py
'''
Imenovanje crteža indeksiranjem 
'''
import numpy as np
import matplotlib.pyplot as plt

naziv = (('Crtež0','Crtež1'),('Crtež2','Crtež3'))

if __name__ == '__main__':
    fig,axs = plt.subplots(2,2,layout='constrained')
    
    for i in range(2):
        for j in range(2):
          axs[i,j].set(title=naziv[i][j],xlabel ='x',ylabel='y')    

    fig.savefig('sl.3.6.pdf')
    fig.show()                          

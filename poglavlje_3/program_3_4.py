# program_3_4.py
'''
Tri pravca u istom crtežu s legendom
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,5])                            

fig, ax = plt.subplots()

ax.set(xlabel='x', ylabel='f(x)', 
       title='Tri pravca i prikaz legende')
ax.plot(x,x, label='x')
ax.plot(x, 5*x, label='5*x')
ax.plot(x, 10*x, label='10*x')
ax.legend(loc='upper left', title='f(x)')
                    
fig.savefig('sl.3.7.pdf')
fig.show()

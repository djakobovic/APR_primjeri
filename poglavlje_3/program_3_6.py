# program_3_6.py
'''
Crtanje odabranog dijela koordinatnog prostora
odredenog atributima xlim i ylim metode set() 
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,201)

fig, ax = plt.subplots()

ax.set(xlabel='x', ylabel='f(x)',
       title='Crtanje u odabranom dijelu koordinatnog prostora',
       xlim=(2.5,3.5), ylim=(5.,45.))
ax.plot(x, 10 * x, 'r-', label='10*x')
ax.plot(x, 3 * x**2, 'b-.',label='3x**2') 
ax.plot(x, x**3, 'k:', label='x**3')
ax.legend(loc='upper left', title='f(x)')   

fig.savefig('sl.3.9.pdf')
fig.show()                                       

# program_3_7.py
'''
Crtanje koordinatnih ravnina s razlicitim mjerilima i
s jednakim mjerilima koordintnih osi atributom aspect='equal'
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,201)

if __name__ == '__main__':
    fig,(ax0,ax1) = plt.subplots(1,2,layout='constrained')

    ax0.set(title='Koordinatna ravnina',
            xlabel='x', ylabel='y',
            xlim=(-5,5), ylim=(-5,5))
    ax0.plot(x, x, 'b-', label=('x'))
    ax0.plot(x, -x, 'r-', label=('-x'))
    ax0.legend(loc='best',title='f(x)')

    ax1.set(title='Koordinatna ravnina',
            xlabel='x', ylabel='y',
            xlim=(-5,5), ylim=(-5,5),
            aspect = 'equal')
    ax1.plot(x, x, 'b-', label=('x'))
    ax1.plot(x, -x, 'r-', label=('-x'))
    ax1.legend(loc='best',title='f(x)')

    fig.savefig('sl.3.10.pdf')
    fig.show()
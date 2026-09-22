# program_3_23.py
'''
Prilagodba crteža uobičajenom matematičkom prikazu.
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi)
y = np.sin(x)
plt.rc('mathtext', fontset='stix')

if __name__ == '__main__':  
    fig,axs = plt.subplots(3,2,layout='constrained')
    '''
    Najjednostavniji pyplot crtež u kojem metoda plot() sama
    kreira okosnice i podjele na okosnicama.
    '''
    axs[0,0].set_title('(1) Uobičajeni pyplot crtež',fontsize=10)
    axs[0,0].plot(x,y)
    '''
    Sve četiri okosnice nisu vidljive i oznake ne postoje
    '''
    axs[0,1].set_title('(2) Crtež bez okosnica i podjeljaka',fontsize=10)
    axs[0,1].set(xticks=[],yticks=[])
    axs[0,1].plot(x,y)
    axs[0,1].spines[['left','right','top','bottom']].set_visible(False)
    '''
    Dvije okosnice nacrtane kao koordinatne osi bez podjeljaka
    '''
    axs[1,0].set_title('(3) Koordinatne osi bez podjeljaka',fontsize=10)
    axs[1,0].set(xticks=[],yticks=[])
    axs[1,0].plot(x,y)    
    axs[1,0].spines[['left', 'bottom']].set_position('center')
    axs[1,0].spines[['top', 'right']].set_visible(False)
    '''
    Dvije okosnice nisu vidlljive, a druge dvije služe
    kao koordinatne osi s podjeljcima koju su automatski kreirani.
    '''
    axs[1,1].set_title('(4) Dvije okosnice kao koordinatne osi',fontsize=10)
    axs[1,1].plot(x,y)    
    axs[1,1].spines[['left', 'bottom']].set_position('center')
    axs[1,1].spines[['top', 'right']].set_visible(False)
    '''
    Određivanje vlastitih podjeljaka metodom kojom se najprije jednim poretkom
    zadaje njihove položaje i zatim drugim poretkom nazive tih podjeljaka.
    '''
    axs[2,0].set_title('(5) Zadavanje vlastitih podjeljaka', fontsize=10)
    axs[2,0].set_xticks([-6,-4,-2,2,4,6],[r'$-6$',r'$-4$',r'$-2$',r'$2$',r'$4$',r'$6$'])
    axs[2,0].set_yticks([-1.0,-0.5,0.5,1.0],[r'$-1.0$',r'$-0.5$',r'$0.5$',r'$1.0$'])
    axs[2,0].plot(x,y)    
    axs[2,0].spines[['left', 'bottom']].set_position('center')
    axs[2,0].spines[['top', 'right']].set_visible(False)
    '''
    Uz koordinatne osi može se metodom text() dodati nazive. 
    '''
    axs[2,1].set_title('(6) Dodavanje naziva koordinatnih osi', fontsize=10)
    axs[2,1].set_xticks([-6,-4,-2,2,4,6],[r'$-6$',r'$-4$',r'$-2$',r'$2$',r'$4$',r'$6$'])
    axs[2,1].set_yticks([-1.0,-0.5,0.5,1.0],[r'$-1.0$',r'$-0.5$',r'$0.5$',r'$1.0$'])
    axs[2,1].plot(x,y)         
    axs[2,1].spines[['left', 'bottom']].set_position('center')
    axs[2,1].spines[['top', 'right']].set_visible(False)
    axs[2,1].text(6.7,0.05,r'$x$',ha='center',va='bottom')
    axs[2,1].text(0.2,1.0,r'$y$',ha='left',va='center')

    fig.savefig('sl.3.25.pdf')
    fig.show()

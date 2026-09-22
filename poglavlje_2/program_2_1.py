# program_2_1.py
'''
Modul numpy za smještanje cijelih brojeva u poredke odabire:
   - četiri bajta, t.j. 32 bita, što se označava kao tip int32 ili
   - osam bajtova, t.j. 64 bita, što se označava kao tip int64.
   po osam bajtova
'''
import numpy as np
# primjeri lista
n = 32
d = [-2**(n-1),2**(n-1)-1]
m = 64
f = [-2**(m-1),2**(m-1)-1]

if __name__ == '__main__':
    p_d = np.array(d, dtype='int32')
    print(f'lista d =     {d}\nporedak p_d = {np.array(d)}          p_d.dtype = {p_d.dtype}')
    e = [d[0], d[1]+1]
    p_e = np.array(e)     
    print(f'lista e =     {e}\nporedak p_e = {np.array(e)}          p_e.dtype = {p_e.dtype}')
    #
    p_f = np.array(f)
    print(f'\nlista f =     {f}\nporedak p_f = {np.array(f)}  p_f.dtype = {p_f.dtype}')
    g = [f[0], f[1]+1]
    p_g = np.array(g)     
    print(f'lista g =     {g}\nporedak p_g = {np.array(g)}            p_g.dtype = {p_g.dtype}')

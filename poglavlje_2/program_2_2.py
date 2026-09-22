# program_2_2.py
'''
Obilježja tipa float
'''
import numpy as np

inf = np.finfo(dtype=float)

if __name__ == '__main__':
    print(f'{inf.bits:30d} broj bitova ')
    print(f'{inf.nmant:30d} broj bitova signifikanda')
    print(f'{inf.iexp:30d} broj bitova eksponenta')
    print(f'{inf.minexp:30d} najmanji eksponent binarne baze')
    print(f'{inf.maxexp:30d} najveći eksponent binarne baze')
    print(f'{inf.max:30} maksimalni broj')
    print(f'{inf.smallest_normal:30} minimalni normirani broj')
    print(f'{inf.smallest_subnormal:30} minimalni denormirani broj')
    print(f'{inf.eps:30} strojni epsilon')
    print(f'{inf.precision:30d} preciznost')


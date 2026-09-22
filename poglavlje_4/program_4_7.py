# program_4_7.py
'''
Provjera ugradenog elektroničkog sata
'''
import time

if __name__ == '__main__':
    print(f'       t[s]                 t[ns]')
    for i in range(10):
        print(f'{time.time():<18}   {time.time_ns()}')

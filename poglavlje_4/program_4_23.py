# program_4_23.py
'''
Primjeri operacija s kompleksnim brojevima
'''

def kompl_oper(z_1,z_2):
    print(f'z_1 =       {z_1}')
    print(f'z_1.real = {z_1.real}    z_1.imag = {z_1.imag}')
    print(f'z_2 =       {z_2}')
    print(f'z_2.real = {z_2.real}    z_2.imag = {z_2.imag}')
    print(f'z_1 + z_2 = {z_1 + z_2}')
    print(f'z_1 - z_2 = {z_1 - z_2}')
    print(f'z_1 * z_2 = {z_1 * z_2}')
    print(f'z_1 / z_2 = {z_1 / z_2}')
    print(f'z_1.conjugate() =                   {z_1.conjugate()}')
    print(f'z_2.conjugate() =                   {z_2.conjugate()}')
    print(f'(z_1.conjugate()).conjugate() =     {(z_1.conjugate()).conjugate()}')
    print(f'(z_2.conjugate()).conjugate() =     {(z_2.conjugate()).conjugate()}')    
    print(f'\n(z_1 + z_2).conjugate() =           {(z_1 + z_2).conjugate()}')
    print(f'z_1.conjugate() + z_2.conjugate() = {z_1.conjugate() + z_2.conjugate()}')
    print(f'\n(z_1 * z_2).conjugate() =           {(z_1 * z_2).conjugate()}')
    print(f'z_1.conjugate() * z_2.conjugate() = {z_1.conjugate() * z_2.conjugate()}')
    print(f'\nz_1 + z_1.conjugate()=              {z_1 + z_1.conjugate()}')
    print(f'2 * z_1.real =                      {2 * z_1.real}')
    print(f'\nz_1 - z_1.conjugate()=              {z_1 - z_1.conjugate()}')
    print(f'2 * z_1.imag =                      {2 * z_1.imag}')

if __name__ == '__main__':    
    z_1 = 2 + 3j
    z_2 = 5 + 7j
    kompl_oper(z_1,z_2)   

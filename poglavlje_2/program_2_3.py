# program_2_3.py
'''
Mjera jedinice zadnjeg mjesta jednaka je eps*2**eks
'''

eps = 2**-52
print(f'\neks = {0}')
for i in range(1,4):
    print(f'{(1.+ i*eps):20.16e} =',end=' ')
    print(f'{(1.+ (i-1)*eps):20.16e} + eps*2**0')
print(f'    .......')
print(f'{(2.-1*eps*2**0):20.16e} = {(2.-2*eps*2**0):20.16e} + eps*2**0')
print(f'{(2.-0*eps*2**0):20.16e} = {(2.-1*eps*2**0):20.16e} + eps*2**0')
print(f'    -------')
print(f'\neks = {1}')
for i in range(1,4):
    print(f'{(1.+ i*eps)*2**1:20.16e} =',end=' ')
    print(f'{(1.+ (i-1)*eps)*2**1:20.16e} + eps*2**1')        
print(f'    .......')
print(f'{(4.-1*eps*2**1):20.16e} = {(4.-2*eps*2**1):20.16e} + eps*2**1')
print(f'{(4.-0*eps*2**1):20.16e} = {(4.-1*eps*2**1):20.16e} + eps*2**1')
print(f'    -------')
print(f'\neks = {2}')
for i in range(1,4):
    print(f'{(1.+ i*eps)*2**2:20.16e} =',end=' ')
    print(f'{(1.+ (i-1)*eps)*2**2:20.16e} + eps*2**2')  
print(f'    .......')
print(f'{(8.-1*eps*2**2):20.16e} = {(8.-2*eps*2**2):20.16e} + eps*2**2')
print(f'{(8.-0*eps*2**2):20.16e} = {(8.-1*eps*2**2):20.16e} + eps*2**2')

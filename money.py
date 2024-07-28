print('Your Balance = $0')
q1 = input('Who was the first person in space? ')
if (q1 == 'Yuri'):
    print('')
    print('Your Balance = $100')
if (q1 != 'Yuri'):
    print('')
    print('Your Balance = $0')


print('')
q2 = input('Who was the first person on the Moon? ')
if (q2 == 'Armstrong' and q1 == 'Yuri'):
    print('')
    print('Your Balance = $175')
if (q2 == 'Armstrong' and q1 != 'Yuri'):                                                            
    print('')
    print('Your Balance = $100')
if (q2 != 'Armstrong' and q1 == 'Yuri'):
    print('')
    print('Your Balance = $75')
if (q2 != 'Armstrong' and q1 != 'Yuri'):
    print('')
    print('Your Balance = $0')


def modulo(a, b):
    r = a
    while r >= b:
        r -= b
    return r

def modulo_rechner():
    print('Modulo Rechner: a % b')
    answer = 'y'
    while answer == 'y':
        a = input('Please enter variable a: ')
        b = input('Please enter variable b: ')
        print('You\'re input: a={}, b={}'.format(a, b))
        a = int(a)
        b = int(b)
        r = modulo(a, b)
        print('{} % {} = {}'.format(a, b, r))
        answer = input('Do you want to do this again? y/n ')
    print('Hau rein, Diggah!')

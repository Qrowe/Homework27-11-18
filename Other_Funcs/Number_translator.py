
a=input('Пожалуйста, введите число, которое хотите перевести:')

def Number_translator(a):

    print('В двоичной системе исчисления данное число будет выглядеть следующим образом:',bin(int(a)))
    print('В восьмеричной системе исчисления данное число будет выглядеть следующим образом:',oct(int(a)))
    print('В шестнадцатиричной системе исчисления данное число будет выглядеть следующим образом:',hex(int(a)))

Number_translator(a)
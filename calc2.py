import os
while True:
    print('select a number')
    print('1.Addition')
    print('2.Subraction')
    print('3.Multiplication')
    print('4.Exit')
    match(input('Enter your choice:')):
       case'1':
        a=int(input('Enter first number:'))
        b=int(input('Enter second number:'))
        print(f'{a}+{b} is {a+b}')
       case'2':
        a=int(input('Enter first number:'))
        b=int(input('Enter second number:'))
        print(f'{a}-{b} is {a-b}')
       case'3':
        a=int(input('Enter first number:'))
        b=int(input('Enter second number:'))
        print(f'{a}*{b} is {a*b}') 
       case'4':
        a=int(input('Enter first number:'))
        b=int(input('Enter second number:'))
        print(f'{a}/{b} is {a/b}') 
       case'5':
        print('exiting...')
        break
       case'_':
        print('Invalid choice')
    input('Press enter to continue...')
    os.system('cls') 
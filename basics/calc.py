import os

while True:
    os.system("cls")
    print("Calculator")
    print('1.➕')
    print('2.➖')
    print('3.❌')
    print('4.Exit')
    ch=input('Select number:')
    if ch=='1':
        a=int(input('Enter value 1:'))
        b=int(input('Enter value 2:'))
        print(f'{a}+{b}={a+b}')
    elif ch=='2':
        x=int(input('Enter value 1:'))
        y=int(input('Enter value 2:'))
        print(f'{x}-{y}={x-y}')
    elif ch=='3':
        p=int(input('Enter value 1:'))
        q=int(input('Enter value 2:'))
        print(f'{p}*{q}={p*q}')
    elif ch=='4':
        print('Bye!')
        break
    else:
        print('Invalid input!!!')
    input('continue')
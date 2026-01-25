## Do a program which takes an integer number as input and tell if its even or odd.
## Faça um programa que leia um número inteiro e diga se é par ou ímpar.

try:
    num = int(input("Enter an integer number: "))
except:
    print("You've done something wrong.")
else:
    if num % 2 == 0:
        print("="*50)
        print(num, "is even.")
        print("="*50)
    else:
        print("="*50)
        print(num, "is odd.")
        print("="*50)

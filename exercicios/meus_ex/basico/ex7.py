## Faça um programa que leia um número inteiro e diga se é par ou ímpar. ##

num = int(input("Insira um número inteiro: "))

if num % 2 == 0:
    print("="*50)
    print(num, "é par.")
    print("="*50)

else:
    print("="*50)
    print(num, "é ímpar.")
    print("="*50)
    
## Faça um programa que leia 3 números e os imprima em ordem crescente.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
num3 = float(input("Insira outro número: "))

num = (num1, num2, num3)

if num1 <= num2 <= num3:
    print("Ordem crescente:", num1, num2, num3)
elif num1 <= num3 <= num2:
    print("Ordem crescente:", num1, num3, num2)
elif num2 <= num1 <= num3:
    print("Ordem crescente:", num2, num1, num3)
elif num2 <= num3 <= num1:
    print("Ordem crescente:", num2, num3, num1)
elif num3 <= num1 <= num2:
    print("Ordem crescente:", num3, num1, num2)
else:  # num3 <= num2 <= num1
    print("Ordem crescente:", num3, num2, num1)

## Faça um programa que leia 3 números e os imprima em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 >= num3:
    print("Ordem decrescente:", num1, num2, num3)
elif num1 >= num3 >= num2:
    print("Ordem decrescente:", num1, num3, num2)
elif num2 >= num1 >= num3:
    print("Ordem decrescente:", num2, num1, num3)
elif num2 >= num3 >= num1:
    print("Ordem decrescente:", num2, num3, num1)
elif num3 >= num1 >= num2:
    print("Ordem decrescente:", num3, num1, num2)
else:  # num3 >= num2 >= num1
    print("Ordem decrescente:", num3, num2, num1)

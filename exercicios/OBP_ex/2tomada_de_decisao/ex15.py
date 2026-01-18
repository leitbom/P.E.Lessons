## Faça um programa que leia 2 números e os imprima em ordem decrescente.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

if num1>num2:
    print(num1,"...", num2)

else:
    print(num2, "..." ,num1)

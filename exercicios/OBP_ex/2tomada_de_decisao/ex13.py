## Faça um programa que leia 2 números e imprima uma mensagem dizendo o maior deles. Detalhe: se os números forem iguais, imprima uma mensagem avisando ao usuário.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

if num1 > num2:
    print(num1, "é o maior")

elif num1 == num2:
    print("Os numeros são iguais!")

else:
    print(num2, "é o maior")

## Faça um programa que leia 3 números e imprima uma das seguintes mensagens:
##· todos os números são iguais.
##· todos os números são diferentes.
##· apenas dois números são iguais.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 and num2 == num3:
    print("Todos os números são iguais")
elif num1 == num2 and num1 != num3 or num1 == num3 and num1 != num2 or num2 == num3 and num2 != num1:
    print("Apenas dois números são iguais")
else:
    print("Todos os números são diferentes")

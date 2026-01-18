## Faça um programa que leia 2 números e imprima uma mensagem dizendo o maior deles.
## Suponha que os números serão diferentes.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

if num1 > num2:
    print(num1, "é o maior")

else:
    print(num2, "é o maior")

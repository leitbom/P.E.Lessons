## Faça um programa que leia 3 números e imprima o valor intermediário, entre o menor e o maior número.
## Suponha que os números serão diferentes.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

while num1 == num2 or num1 == num3 or num2 == num3:
    print("Insira valores diferentes para cada número:")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

if num1 <= num2 <= num3:
    print(num2)
elif num1 <= num3 <= num2:
    print(num3)
elif num2 <= num1 <= num3:
    print(num1)
elif num2 <= num3 <= num1:
    print(num3)
elif num3 <= num1 <= num2:
    print(num1)
else:  # num3 <= num2 <= num1
    print(num2)

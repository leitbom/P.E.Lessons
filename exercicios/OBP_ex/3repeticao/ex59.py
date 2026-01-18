## Faça um programa que calcule o resultado de num1//num2 utilizando o algoritmo de subtrações sucessivas. 
## num1 e num2 devem ser lidos da entrada. 
## Informe ao usuário caso a divisão não seja exata. 
## Exemplo: valores lidos: 6 3
##          impressão: 2
##          dica: 6 - 3 = 3 - 3 = 0
##          (2 subtrações)

num1 = int(input("Insira um número inteiro maior que zero: "))
num2 = int(input("Insira um número inteiro maior que zero e menor que o primeiro número inserido: " ))

while num1<=num2 or num1==0 or num2==0:
    num1 = int(input("Insira um número inteiro maior que zero: "))
    num2 = int(input("Insira um número inteiro maior que zero e menor que o primeiro número inserido: " ))

for n in range(num1,-1,-num2):
    num -= n

if print(n)==0:
    print("Divisão inteira")

else:
    print("Divisão não inteira")

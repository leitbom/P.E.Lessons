## Faça um programa que calcule o produto de 2 números lidos da entrada (num1 e num2) através dp método de somas sucessivas. 
## Suponha que num1 e num2 são positivos.
## Exemplo: valores lidos: 3 4
##          impressão:     12
##          dica:          3 x 4 = 3 + 3 + 3 + 3 = 12

num1 = int(input("Insira um número inteiro maior que zero: "))
num2 = int(input("Insira um número inteiro maior que zero: " ))
soma = 0

for n in range(num2):
    soma += num1

print(soma)

# Acho que...é isso?

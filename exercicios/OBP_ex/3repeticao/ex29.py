## Faça um programa que leia um número da entrada e imprima os números naturais de 0 até este número. 
## Suponha que o número lido da entrada será maior que zero.

num = int(input("Insira um número maior que zero: "))

# Forçando o usuário a inserir um número válido

while num <= 0:
    num = int(input("Insira um número maior que zero: "))

for n in range(num+1):
    print(n)

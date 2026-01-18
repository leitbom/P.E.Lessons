## Faça um programa que leia um número da entrada e imprima os números ímpares menores do que este número.

num = int(input("Insira um número: "))

if num>=0:
    for n in range(num):
        if n%2!=0:
            print(n)
else:
    for n in range(num+1,0):
        if n%2!=0:
            print(n)

# O exercício não deixou claro se era para os positivos e negativos...
# Então eu fiz pros dois...

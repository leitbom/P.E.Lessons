## Faça um programa que imprima os termos de uma P.A., sendo lidos da entrada: o primeiro termo (a0), a razão (r) e o número de elementos (num).

a0 = int(input("Insira um número inteiro para início da PA: "))
r = int(input("Insira um número inteiro para razão: "))
num = int(input("Insira um número inteiro maior que zero para o número de elementos da PA: "))

# Evita que o usuário insira um número indesejado na variável num

while num<=0:
    num = int(input("Insira um número inteiro maior que zero para o número de elementos da PA: "))

# Lista para depois imprimir sequência na mesma linha

listaPA = []

for n in range(num):
    listaPA.append(a0 + (r*n))

for elemento in listaPA: 
    print(elemento,end=" ")

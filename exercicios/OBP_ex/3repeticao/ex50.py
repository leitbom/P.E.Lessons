## Faça um programa que leia um número da entrada (num), a seguir leia num números da entrada e imprima o maior deles.

num = int(input("Quantos números você deseja inserir? "))

lista_num = []

# Forçar o usuário a inserir um número inteiro positivo

while num<0:
    num = int(input("Quantos números você deseja inserir?(Insira um número inteiro positivo) "))

for n in range (num):
    numl = int(input("Insira um número inteiro: "))
    lista_num.append(numl)

# Para imprimir o maior número contido na lista_num

print("O maior número inserido foi",max(lista_num))

# Mas eu já não fiz isso???

## Faça um programa que leia um número da entrada (num), a seguir leia num números da entrada e imprima o maior, o menor e soma dos números lidos.

num = int(input("Quantos números você deseja inserir? "))

lista_num = []

# Forçar o usuário a inserir um número inteiro positivo

while num<0:
    num = int(input("Quantos números você deseja inserir?(Insira um número inteiro positivo) "))

for n in range (num):
    numl = int(input("Insira um número inteiro: "))
    lista_num.append(numl)

# Para imprimir o maior, menor e soma dos números contido na lista_num

print("O maior número inserido foi",max(lista_num))
print("O menor número inserido foi",min(lista_num))
print("A soma dos números lidos é",sum(lista_num))

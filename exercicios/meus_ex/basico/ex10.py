## Faça um programa que leia um número da entrada (num). ## 
## A seguir leia num números da entrada e imprima o maior deles. ##


print("="*50)
num = int(input("Quantos números queres comparar? "))
print("="*50)

lista_num = []

while num <= 0:
    num = int(input("Insira um número inteiro positivo: "))
    print("="*50)

for n in range(num):
    num2 = float(input("Insira qualquer número: "))
    print("="*50)
    lista_num.append(num2)

print("O maior número inserido foi ==> ", max(lista_num))

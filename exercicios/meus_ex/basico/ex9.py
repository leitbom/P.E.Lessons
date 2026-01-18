## Faça um programa que leia um número (num) inteiro e um intervalo da entrada (início e fim). ##
## O programa deve imprimir os múltiplos de num neste intervalo. ##

print("="*60)
num_1 = int(input("Defina o início do intervalo: "))
print("="*60)
num_2 = int(input("Defina o final do intervalo: "))
print("="*60)
num = int(input("Introduza um número inteiro para fator comum da verificação: "))
print("="*60)

lista_n = []

while num == 0 or num_1==num_2:
    num_1 = int(input("Defina o início do intervalo: "))
    print("="*60)
    num_2 = int(input("Defina o final do intervalo: "))
    print("="*60)
    num = int(input("Introduza um número inteiro para fator comum da verificação: "))
    print("="*60)

if num_1 < num_2:    
    for n in range(num_1, num_2 + 1):
        if n % num == 0:
            lista_n.append(n)

else:
    for n in range(num_2, num_1 + 1):
        if n % num == 0:            
            lista_n.append(n)

print("Múltiplos =",end=" ")

for elemento in lista_n:
    print(elemento, end=" ")


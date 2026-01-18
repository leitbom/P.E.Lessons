## Faça um programa que leia um número daentrada (num), imprima os números de 1 a num e o seu somatório.

num = int(input("Insira um número inteiro maior que zero: "))

while num<=0:
    num = int(input("Insira um número inteiro maior que zero: "))

somatorio = 0

for n in range(1,num+1):
    somatorio += n
    print(n)

print("Somatório = ",somatorio)

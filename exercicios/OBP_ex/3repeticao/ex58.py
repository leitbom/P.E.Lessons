## Faça um programa que leia 2 números da entrada e imprima o resto da divisão inteira do primeiro pelo segundo usando subtrações sucessivas.

num1 = int(input("Insira um número inteiro maior que zero: "))
num2 = int(input("Insira um número inteiro maior que zero e menor que o primeiro número inserido: " ))

num = num1

while num1<num2 or num1==0 or num2==0:
    num1 = int(input("Insira um número inteiro maior que zero: "))
    num2 = int(input("Insira um número inteiro maior que zero e menor que o primeiro número inserido: " ))

for n in range(num1,-1,-num2): # determinar intervalo e passos dentro desse intervalo e faça n vezes
    num -= n # subtraia do num1 a distância do pulo que eu dei no intervalo n vezes
print("Resto de divisão inteira = ",n) # Mostre o resto da divisão??

# Acho que...é isso?
# Se deu certo nem mexo

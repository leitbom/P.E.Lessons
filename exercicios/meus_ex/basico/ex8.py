## Faça um programa que leia um número inteiro e imprima os números de 0 a num na mesma linha ##

num = int(input("Insira um número inteiro: "))
lista_num = []
contador = 0

if num > 0:
    for n in range(0, num+1):
        lista_num.append(contador)
        if contador != num:
            contador += 1

    for elemento in lista_num:
        print(elemento, end = " ")
        
else:
    for n in range(0, num-1, -1):
        lista_num.append(contador)
        if contador != num:
            contador -= 1

    for elemento in lista_num:
        print(elemento, end = " ")

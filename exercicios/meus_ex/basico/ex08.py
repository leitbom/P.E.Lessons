## Do a programa wich take an integer number and print the numbers from 0 to num on the same line.
## Faça um programa que leia um número inteiro e imprima os números de 0 a num na mesma linha.

try:
    num = int(input("Enter an integer number: "))
except:
    print("You've done something wrong.")
else:
    lista_num = []
    contador = 0
    if num > 0:
        for n in range(0, num+1):
            lista_num.append(contador)
            if contador != num:
                contador += 1       
    else:
        for n in range(0, num-1, -1):
            lista_num.append(contador)
            if contador != num:
                contador -= 1

    for elemento in lista_num:
        print(elemento, end = " ")

## Faça um programa que leia um intervalo da entrada (início e fim) e imprima os números naturais neste intervalo.
## Exemplo: valores lidos: 5 9
##          impressão: 5 6 7 8 9

ei = int(input("Insira um valor para início do intervalo: "))
ef = int(input("Insira um valor para fim do intervalo: "))



if ei<ef:
    for n in range(ei,ef+1):
        print(n)
elif ei == ef:
    print(0)
else:
    for n in range(ef,ei+1):
        print(n)

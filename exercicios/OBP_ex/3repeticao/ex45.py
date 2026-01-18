## Faça um programa que leia um intervalo da entrada (início e fim) e imprima os números pares entre início e fim e seu somatório.

ei = int(input("Insira um número inteiro para início do intervalo: "))
ef = int(input("Insira um número inteiro para fim do intervalo: "))
d = 2

somatorio = 0

if ei<ef: # intervalo normal
    for n in range(ei,ef+1):
        if n % d == 0:
            somatorio += n
    print(somatorio)

elif ei == ef: # sem intervalo
    print(0)
    
else: # intervalo invertido
    for n in range(ef,ei+1):
        if n % d == 0:
            somatorio += n
    print(somatorio)

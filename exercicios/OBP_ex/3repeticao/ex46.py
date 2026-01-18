## Faça um programa que leia um número (num) da entrada e imprima os múltiplos de 3 e 5 ao mesmo tempo no intervalo de 1 a num.

ei = 1
ef = int(input("Insira um número inteiro para fim do intervalo: "))
d = 15

if ei<ef: # intervalo normal
    for n in range(ei,ef+1):
        if n % d == 0:
            print(n)

elif ei == ef: # sem intervalo
    print(0)
    
else: # intervalo invertido
    for n in range(ef,ei+1):
        if n % d == 0:
            print(n)

## Faça um programa que leia um intervalo da entrada (início e fim) e um número (num). 
## O programa deve imprimir os múltiplos de num entre início e fim.

ei = int(input("Insira um número inteiro para início do intervalo: "))
ef = int(input("Insira um número inteiro para fim do intervalo: "))
d = int(input("Insira um número inteiro para ser o fator comum do intervalo:"))

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

# Tá ficando chato fazer isso....talvez uma pausa para um café?
# Reaproveitar o código é bem útil, me poupa ter que ficar escrevendo, cometendo erros burros e pensar demais.
# Café é muito bom também

## (Prova 1 - 95/2) A série de RICCI é gerada da seguinte forma:
## Os dois primeiros termos são fornecidos pelo usuário, a partir  daí, os termos são gerados como a soma dos dois termos anteriores, ou seja, ai=ai-1+ai-2 para i≥3. 
## Escreva um programa que imprima os N (N lido e >= 2) primeiros termos da série de RICCI.
## O programa deve imprimir, também a soma dos termos impressos.

term1 = float(input("Insira o primeiro termo da sequência: "))
term2 = float(input("Insira o segundo termo da sequência: "))
n = int(input("Insira quantos termos da sequência deseja (número inteiro maior que 2): "))

listat = [term1, term2]

# Loop para usuário cumprir requisitos da sequência

while n <= 2 or term1>term2:
    term1 = int(input("Insira o primeiro termo da sequência: "))
    term2 = int(input("Insira o segundo termo da sequência: "))
    n = int(input("Insira quantos termos da seuência deseja (número inteiro maior que 2): "))

# Adicionar novo termo ao final da lista e repetir esse processo n-2 vezes

for i in range(n-2):
    listat.append(listat[-1]+listat[-2])

# Impressão de resultados desejados

print("Sequência =",listat)
print("Soma dos termos da sequência =",sum(listat))

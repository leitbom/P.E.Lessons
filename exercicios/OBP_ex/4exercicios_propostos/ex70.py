## (Prova 1 - 96/1) A série de FETUCCINE é gerada da seguinte forma:
## * os dois primeiros termos são fornecidos pelo usuário;
## * os termos seguintes são gerados como a soma ou subtração dos dois termos anteriores, ou seja:
## ai = a(i - 1) + a(i - 2) ==> para i ímpar
## ai = a(i - 1) - a(i - 2) ==> para i par
## Escreva um programa que imprima os N (N >= 2) primeiros termos da série de FETUCCINE.
## O programa deve imprimir, também a soma dos termos impressos.


# Fazer a mesma coisa que no exercício anterior, mas muda a fórmula se for par/ímpar

term1 = float(input("Insira o primeiro termo da sequência: "))
term2 = float(input("Insira o segundo termo da sequência: "))
n = int(input("Insira quantos termos da seuência deseja (número inteiro maior que 2): "))

listat = [term1, term2]

# Loop para usuário cumprir requisitos da sequência

while n <= 2 or term1>term2:
    term1 = int(input("Insira o primeiro termo da sequência: "))
    term2 = int(input("Insira o segundo termo da sequência: "))
    n = int(input("Insira quantos termos da sequência deseja (número inteiro maior que 2): "))

# Adicionar novo termo ao final da lista e repetir esse processo n-2 vezes
# Dentro do loop uma condicional if/else para filtrar números ímpares e pares

for i in range(n-2):
    if listat[-1]%2!=0:
        listat.append(listat[-1]+listat[-2])
    else:    
        listat.append(listat[-1]-listat[-2])

# Impressão de resultados desejados

print("Sequência =",listat)
print("Soma dos termos da sequência =",sum(listat))

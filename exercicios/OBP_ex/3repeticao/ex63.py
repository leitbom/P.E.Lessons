## Escreva um algoritmo que leia uma seqüência de 50 números naturais e imprima o maior número da seqüência múltiplo de 2 e de 3 ao mesmo tempo.

# Ler uma sequência de 50 números??? como assim é para o usuário a inserir a sequência manualmente?

listan = []

for n in range(50):
    num = int(input("Insira um número."))

    if num%6==0:
        listan.append(num)

print(max(listan))

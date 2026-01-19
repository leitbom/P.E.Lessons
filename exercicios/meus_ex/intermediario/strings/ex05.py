## Faça um programa que leia uma string.
## Imprima a string em formato de escada invertida.

texto = str(input("Insira uma string: "))

for char in texto:
    texto %= 10
    print(texto)
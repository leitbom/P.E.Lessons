## Faça um programa que leia uma string.
## Mostre a string de trás para frente utilizando somente letras maiúsculas.

texto = str(input("Insira uma string: "))

print(texto.upper()[::-1])
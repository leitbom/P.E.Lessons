## Do a program that reads a string.
## Show the string backwards using only uppercase letters.
## Faça um programa que leia uma string.
## Mostre a string de trás para frente utilizando somente letras maiúsculas.
try:
    texto = str(input("Enter a string: "))
    print(texto.upper()[::-1])
except KeyboardInterrupt:
    print("You interrupted the program.")

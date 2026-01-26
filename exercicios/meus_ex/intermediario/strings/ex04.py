## Do a program that reads a string.
## Print the string in a staircase format.
## Faça um programa que leia uma string.
## Imprima a string em formato de escada.

try:
    texto = str(input("Enter a string: "))
    txt = ""
    for char in texto:
        txt += char
        print(txt)
except KeyboardInterrupt:
    print("You interrupted the program.")

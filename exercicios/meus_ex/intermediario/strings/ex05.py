## Do a program that reads a string.
## Print the string in an inverted staircase format.
## Faça um programa que leia uma string.
## Imprima a string em formato de escada invertida.
try:
    texto = str(input("Enter a string: "))
    print(texto)

    for char in texto:
        texto = texto[:-1]
        print(texto)
except KeyboardInterrupt:
    print("You interrupted the program.")

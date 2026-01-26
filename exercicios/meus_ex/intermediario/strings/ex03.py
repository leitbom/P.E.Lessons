## Do a program that reads a string 
## Imprima verticalmente caractere por caractere
## Faça um programa que leia uma string 
## Imprima verticalmente caractere por caractere
try:
    texto = str(input("Enter a string: "))

    for char in texto:
        print(char)
except KeyboardInterrupt:
    print("You interrupted the program.")
    
## Do a program that reads a string and tells if it is a palindrome or not.
## The program must ignore case differences and anything that is not a letter.
## Faça um programa que leia uma string e diga se é um palíndromo ou não
## O programa deve ignorar se a string contém diferenças de tamanhos de letras e tudo que não for letras.
try:
    texto = str(input("Insira uma string:")) # input string
    texto = texto.upper() # manipulation to uppercase

    for char in texto: # for each character in string
        if char.isupper()==True: # if character is a uppercase letter
            continue
        else: # else replace character with empty string
            texto = texto.replace(char,"")
    while texto == "": # while string is empty
        print(False)
        break  
    else:  # else continue with the program
        if texto == texto[::-1]: # if it is a palindrome return True
            print(True)
        else: # if not return False
            print(False)
except:
    print("Something went wrong.")
        
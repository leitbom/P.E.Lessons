## Do a function wich takes a string and a number as inputs by the user.
## The function must return the concatenation and interpolation by string and number.
## Crie uma função capaz de ler uma string e um número inseridos pelo usuário.
## A função deve retornar a concatenação e interpolação da string com o número.

def strnum():
    try:
        text = str(input("Enter a string: "))
        num = int(input("Enter an integer number:"))
        if num < 0:
            print("Concatenation ==>",text + str(num))
            print("Impossible interpolation")
        else:
            print("Concatenation ==>",text + str(num))
            print("Interpolation ==>",text * num)
    except:
        print("You've done something wrong.")
strnum()

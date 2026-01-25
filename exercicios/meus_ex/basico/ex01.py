### shame on me
## Do a program who lets the user input a integer number.
## Verify if the number is a prime and return a message to the user.
## Faça um programa que permita o usuário inserir um número inteiro .
## Verifique se ele é primo e retorne uma mensagem ao utilizador.

try:
    num = int(input("Enter a integer number: "))
except:
    print("You've done something wrong.")
else:
    if num <= 1:
        print("Not prime")
    else:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            print("PRIME")
        else:
            print("Not prime")

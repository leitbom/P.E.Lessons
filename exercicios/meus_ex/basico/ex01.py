###
## (Do a program who lets the user input a integer number)
## Faça um programa que permita o usuário inserir um número inteiro 
## (Verify if the number is a prime and return a message to the user)
## Verifique se ele é primo e retorne uma mensagem ao utilizador


# Tive que pedir ajuda à IA pois meu cérebro estava derretendo...
# Deve funcionar bem para números grandes também....
# eu programa demorava muito para verificar números com mais de 10 casas decimais...
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




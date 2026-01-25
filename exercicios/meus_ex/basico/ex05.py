## Do a program which takes two numbers as inputs and print a message telling wich one is the greatest.
## If numbers are equal, print a message warning the user.
## Faça um programa que leia dois números e imprima uma mensagem dizendo qual deles é o maior.
## Se os números forem iguais, imprima uma mensagem avisando o usuário.

try:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter a number: "))
except:
    print("You've done something wrong.")
else:
    if num_1 == num_2:
        print("="*50)
        print("The numbers are equal.")
        print("="*50)
    else:
        if num_1 > num_2:
            print("="*50)
            print("The greatest number is", num_1)
            print("="*50)
        else:
            print("="*50)
            print("The greatest number is", num_2)
            print("="*50)

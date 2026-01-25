## Do a program wich takes a number as input (num).
## Next, take num numbers as input and print the greatest.
## Faça um programa que leia um número da entrada (num). 
## A seguir, leia num números da entrada e imprima o maior.

try:
    print("="*50)
    num = int(input("How many numbers do you want to input? "))
    print("="*50)
    lista_num = []
    while num <= 0:
        num = int(input("Please insert a positive integer number: "))
        print("="*50)
    for n in range(num):
        num2 = float(input("Enter a number: "))
        print("="*50)
        lista_num.append(num2)
except:
    print("You've done something wrong.")
else:
    if max(lista_num)==min(lista_num): # If all numbers are equal wich one is the greatest? None
        print("They're all equal.")
    else:
        print("The greatest number you entered was", max(lista_num))

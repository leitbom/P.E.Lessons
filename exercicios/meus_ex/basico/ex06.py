## Do a program wich takes two integer numbers as input.
## Do the arithmetic mean of the sum of those numbers and the integer numbers betwen them.
## Faça um programa que leia dois números inteiros.
## Faça a média aritmética da soma destes números e dos números inteiros entre eles.

try:
    num_1 = int(input("Enter a integer number: "))
    num_2 = int(input("Enter a integer number: "))
except:
    print("You've done something wrong.")
else:
    listan = [num_1,num_2]
    media = sum(listan)/len(listan)
    if num_1>num_2:
        for n in range(num_2,num_1+1):
            listan.append(n)
    elif num_1==num_2:
        print("Arithmetic mean of total sum =", num_1) 
    else:
        for n in range(num_1,num_2+1):
            listan.append(n)
    print("Arithmetic mean of total sum =",media)

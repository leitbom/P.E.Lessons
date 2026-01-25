## Do a program which accept a number input and print its predecessor and successor.
## Faça um programa que leia um número da entrada e imprima seu antecedente e seu sucessor.

try:
    num = float(input("Enter a number: "))
except:
    print("You've done something wrong.")
else:
    print("="*50)
    print("predecessor = ",num - 1)
    print("="*50)
    print("successor = ",num + 1)
    print("="*50)

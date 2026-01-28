## Do a program that calculates and prints the terms of the series X**N/N! where X and N should be read from the input.
## Faça um programa que calcule e imprima os termos da série X**N/N! onde X e N devem ser lidos da entrada.

try:
    x = float(input("Enter a number: "))
    n = int(input("Enter an integer number: "))
    from math import factorial as fa
    result  = x**n/fa(n)
except:
    print("You've done something wrong.")
else:
    print(f'{result:.2f}')

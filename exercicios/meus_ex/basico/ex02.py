## Do a program capable of taking the value of two integer numbers and showing the results of the following operations:
## sum, subtraction, multiplication, division, exponentiation and integer division.
## Faça um programa que leia o valor de dois numeros inteiros e mostre o resultado de sua:
## soma, subtração, multiplicação, divisão, exponenciação e divisão inteira.

try:
    variavel_1 = int(input("Enter a integer value to the first variable: "))
    variavel_2 = int(input("Enter a integer value to the second variable: "))
except:
    print("You've done something wrong.")
else:
    soma = variavel_1 + variavel_2
    sub = variavel_1 - variavel_2
    mult = variavel_1 * variavel_2
    exp = variavel_1 ** variavel_2
    if variavel_2 == 0:
        print("="*50)
        print("Sum =", soma)
        print("="*50)
        print("Subtraction =", sub)
        print("="*50)
        print("Multiplication =", mult)
        print("="*50)
        print("Exponentiation =", exp)
        print("="*50)
        print("Impossible Division")
        print("="*50)
        print("Impossible division, so no remainder")
        print("="*50)
    else:
        print("="*50)
        print("Sum =", soma)
        print("="*50)
        print("Subtraction =", sub)
        print("="*50)
        print("Multiplication =", mult)
        print("="*50)
        print("Exponentiation =", exp)
        print("="*50)
        divint = variavel_1 // variavel_2
        print("Integer Division =", divint)
        print("="*50)
        rest = variavel_1 % variavel_2
        print("Remainder =", rest)
        print("="*50)

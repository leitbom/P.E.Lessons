## Do a program doing the same as exercice 2, but working with floating numbers.
## Faça um programa igual o do exercício 2, mas que trabalhe com números racionais.

try:
    variavel_1 = float(input("Enter a floating point value to the first variable: "))
    variavel_2 = float(input("Enter a floating point value to the second variable: "))
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
        divfloat = variavel_1 / variavel_2
        print("Division =", divfloat)
        print("="*50)

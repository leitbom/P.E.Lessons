## Faça um programa igual o do exercício 2, mas que trabalhe com números racionais ##
## Soma, subtração (do primeiro pelo segundo), multiplicação, exponenciação e divisão racional(do primeiro pelo segundo) ##

variavel_1 = float(input("Atribua um valor inteiro para a primeira variável: "))
variavel_2 = float(input("Atribua um valor inteiro para a segunda variável: "))

soma = variavel_1 + variavel_2
sub = variavel_1 - variavel_2
mult = variavel_1 * variavel_2
exp = variavel_1 ** variavel_2

if variavel_2 == 0:
    print("="*50)
    print("Soma =", soma)
    print("="*50)
    print("Subtração =", sub)
    print("="*50)
    print("Multiplicação =", mult)
    print("="*50)
    print("Exponenciação =", exp)
    print("="*50)
    print("Divisão inpossível")
    print("="*50)
    
else:
    print("="*50)
    print("Soma =", soma)
    print("="*50)
    print("Subtração =", sub)
    print("="*50)
    print("Multiplicação =", mult)
    print("="*50)
    print("Exponenciação =", exp)
    print("="*50)
    divfloat = variavel_1 / variavel_2
    print("Divisão =", divfloat)
    print("="*50)

## Faça um programa que leia o valor de dois numeros inteiros e mostre o resultado de sua: ##
## soma, subtração(do primeiro pelo segundo), multiplicação, divisão, exponenciação(do primeiro pelo segundo) e divisão inteira (do primeiro pelo segundo) ##

variavel_1 = int(input("Atribua um valor inteiro para a primeira variável: "))
variavel_2 = int(input("Atribua um valor inteiro para a segunda variável: "))

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
    print("Divisão inexistente, sem resto de divisão")
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
    divint = variavel_1 // variavel_2
    print("Divisão inteira =", divint)
    print("="*50)
    rest = variavel_1 % variavel_2
    print("Resto de divisão inteira =", rest)
    print("="*50)

## Faça um programa que leia um número da entrada e imprima uma mensagem dizendo se o número é solução da equação 2 x ** 2 - 7 * x + 3 = 0. 

x = float(input("Insira um número para verificação: "))

if ((2*(x**2)) - (7*x) + 3) == 0:
    print("É solução da equação!")

else:
    print("Não é solução da equação")

# As soluções são 0.5 e 3, qualquer outro valor inserido vai retornar else.

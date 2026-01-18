## Faça um programa que leia da entrada um número e imprima o seu valor absoluto (sem o sinal).

num = float(input("Insira um número"))

valor_absoluto = num

if num<0:
    valor_absoluto = -1 * num
    print(valor_absoluto)

else:
    valor_absoluto = num
    print(valor_absoluto)

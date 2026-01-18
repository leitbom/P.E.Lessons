###
##  Faça um programa que calcule o M.D.C entre dois números lidos da entrada.

num_1 = int(input("Insira um número inteiro maior que 1: "))
num_2 = int(input("Insira um número inteiro maior que 1: "))

while num_1 <= 1 or num_2 <= 1:
    print("Números devem ser maiores que 1.")
    num_1 = int(input("Insira um número inteiro maior que 1: "))
    num_2 = int(input("Insira um número inteiro maior que 1: "))

a, b = num_1, num_2
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

mdc = a
print("MDC =", mdc)
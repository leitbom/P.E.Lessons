###
## Faça um programa que leia um número da entrada e imprima os termos da série de Fibonacci menores que este valor.

num = int(input("Digite um número: "))

a, b = 0, 1

while a < num:
    print(a, end=' ')
    a, b = b, a + b

# pensei demais...ou de menos :-(

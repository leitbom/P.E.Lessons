## Faça um programa que leia um número da entrada (num) e imprima os num primeiros números pares.

num = int(input("Insira um número inteiro maior que zero: "))

# listando pro esquema de por tudo na mesma linha kkk...

listan = []

while num<=0:
    num = int(input("Insira um número inteiro maior que zero: "))

for n in range(num*2):
    if n % 2 == 0:
        listan.append(n)

# Só pra imprimir na mesma linha

for e in listan:
    print(e, end=" ")

# Eu sinto que eu meio que roubei nesse exercício....
# Acho que era pra resolver usando loop while mas que se foda...deu certo no final

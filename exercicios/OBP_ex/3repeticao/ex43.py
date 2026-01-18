## Faça um programa que leia um intervalo da entrada (início e fim) e imprima os múltiplos de 5 entre eles.
## Observação: o que acontece se fim for menor que início? Seu programa continua funcionando?

ei = int(input("Insira um valor para início do intervalo: "))
ef = int(input("Insira um valor para fim do intervalo: "))

if ei<ef:
    for n in range(ei,ef+1):
        if n % 5 == 0:
            print(n)
elif ei == ef:
    print(0)
else:
    for n in range(ef,ei+1):
        if n % 5 == 0:
            print(n)


# Quer em ordem crescente, decrescente, na mesma linha e com queijo extra senhor?

## Faça um programa que leia um número da entrada (limite), um incremento (incr) e imprima os números naturais de 0 até limite pulando de incr.
## Suponha que o limite e incr são maiores que zero

limite = int(input("Insira um valor maior que zero para o limite: "))
incr = int(input("Insira um valor maior que zero para o incremento: "))

# Prendendo o usuário em um loop até inserir um valor desejado...

while limite<0 or incr<0:

    limite = int(input("Insira um valor maior que zero para o limite: "))
    incr = int(input("Insira um valor maior que zero para o incremento: "))


for n in range(0,limite,incr):
    print(n)

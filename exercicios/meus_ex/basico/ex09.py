## Do a program wich takes a integer number (num) and an input interval (beginning and end).
## This program should be able to print the multiples of num in the interval.
## Faça um programa que leia um número inteiro (num) e um intervalo da entrada (início e fim).
## O programa deve imprimir os múltiplos de num neste intervalo.

try:
    print("="*60)
    num_1 = int(input("Define the beginning of the interval: "))
    print("="*60)
    num_2 = int(input("Define the end of the interval: "))
    print("="*60)
    num = int(input("Enter an integer number for the multiples verification: "))
    print("="*60)
except:
    print("Could you stop trying this?")
else:
    lista_n = []
    while num == 0:
        num = int(input("Nice try, try something other than zero: "))
        print("="*60)
    if num_1 < num_2:    
        for n in range(num_1, num_2 + 1):
            if n % num == 0:
                lista_n.append(n)
    else:
        for n in range(num_2, num_1 + 1):
            if n % num == 0:            
                lista_n.append(n)
    print("Multiples =",end=" ")
    for elemento in lista_n:
        print(elemento, end=" ")

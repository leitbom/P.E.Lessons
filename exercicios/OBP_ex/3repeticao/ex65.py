## Faça um programa que leia um número (num) da entrada e imprima os num primeiros termos da série de Fibonacci.

num = int(input("Insira o número de elementos da sequência de Fibonacci que quer ver: "))

fibo = [1,1] # é necessário inserir os dois primeiros elementos manualmente na lista 

for n in range(num-2):
    fibo.append(fibo[-1]+fibo[-2]) # é necessário fazer a contagem inversa dos elementos

print(fibo)

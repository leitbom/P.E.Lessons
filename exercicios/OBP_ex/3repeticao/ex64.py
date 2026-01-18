## Faça um programa que imprima os 10 primeiros termos da série de Fibonacci.

## Observação: a0 = 1
##             a1 = 1
##             an = an - 1 + a(n - 2)

fibo = [1,1] # é necessário inserir os dois primeiros elementos manualmente na lista.

for n in range(8):
    fibo.append(fibo[-1]+fibo[-2]) # é necessário fazer a contagem inversa dos elementos

print(fibo)

# Dá pra melhorar a forma de imprimir, mas que se f***...

## Faça um programa que leia um número da entrada (num) e imprima a soma dos números pares entre 1 e num. 
## Suponha que num será maior que zero.

num = int(input("Insira um número inteiro maior que zero: "))
somatorio = 0

while num<=0:
    num = int(input("Insira um número inteiro maior que zero: "))


for n in range(1,num+1):
    if n % 2 == 0:
        somatorio += n 

print("Somatório dos pares entre 1 e",num,"=", somatorio)

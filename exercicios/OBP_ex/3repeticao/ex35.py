## Faça um programa que leia um número da entrada e imprima a tabuada deste número. 
## Suponha que o número lido da entrada é maior que zero.

num = int(input("Insira um número maior que zero: "))

while num <= 0:
    num = int(input("Insira um número maior que zero: "))

for n in range(1,11):
    print(num,"x",n,"=",num*n)
    
## Faça um programa que leia um número da entrada (num) e imprima o somatório dos num primeiros números ímpares.

num = int(input("Insira um número inteiro maior que zero: "))
somatorio = 0

while num<=0:
    num = int(input("Insira um número inteiro maior que zero: "))


for n in range(1,(num*2)+1): # essa bagunça até que deu certo
    if n % 2 != 0:
        somatorio += n 
        print(n) # ajuda a compreender quais números foram somados

print("Somatório =", somatorio)

# Novamente eu sinto que era pra eu usar um contador e ir trabalhando com while...
# Mas funcionou novamente...então...que se foda

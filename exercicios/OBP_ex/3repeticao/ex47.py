## Faça um programa que leia um número da entrada, calcule e imprima o seu fatorial. 
## Lembre-se que: n! = n x (n -1) x (n - 2) x ... x 1
##                0! = 1 e 1! = 1


num = int(input("Insira um número inteiro positivo: "))

fatorial = 1

# Prender usuário em loop para não inserir numeros negativos

while num<0:
    num = int(input("Insira um número inteiro positivo: "))

# Cáculo de fatorial    

for n in range(num,1-1,-1):
    fatorial *= n
    
print(fatorial)

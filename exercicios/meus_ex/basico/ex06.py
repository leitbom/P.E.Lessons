## Faça um programa que leia dois números inteiros ##
## Faça a média aritmética da soma destes números e dos números inteiros entre eles ##

num_1 = int(input("Atribua um valor para o primeiro número: "))
num_2 = int(input("Atribua um valor para o segundo número: "))

listan = [num_1,num_2]
media = sum(listan)/len(listan)

if num_1>num_2:
    for n in range(num_2,num_1+1):
        listan.append(n)
elif num_1==num_2:
    print("Média dos valores do intervalo =", num_1) 

else:
    for n in range(num_1,num_2+1):
        listan.append(n)

print("Média da soma total =",media)

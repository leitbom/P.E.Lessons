## Faça  um  programa  que  imprima  os  termos  de uma  P.G. 
## Sendo  lidos  da  entrada:  o  primeiro  termo (a0), a razão (q) e o número de elementos (num).

a0 = int(input("Insira um número inteiro para início da PG: "))
q = int(input("Insira um número inteiro para razão: "))
num = int(input("Insira um número inteiro maior que zero para o número de elementos da PG: "))

# Evita que o usuário insira um número indesejado na variável num

while num<=0:
    num = int(input("Insira um número inteiro maior que zero para o número de elementos da PG: "))

# Lista para depois imprimir sequência na mesma linha

listaPG = []

# Para cada número no intervalo (1 - num+1)
# a0*(q**(n-1)) ==> fórmula do elemento da PG
# Cada vez que o n mudar o valor do expoente vai alterar o resultado gerando o próximo elemento da PG sucessivamente

for n in range(1,num+1):
    listaPG.append(a0 * q**(n-1)) # adiciona à lista

for elemento in listaPG:
    print(elemento,end=" ")

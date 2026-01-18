## Faça um programa que leia uma seqüência de números terminada por 0 e imprima a média aritmética dos ímpares e a soma dos pares.

# Criar lista para conter números inseridos com um elemento diferente de zero.
# Criar listas para conter números pares e ímpares.

num = [1]
lista_num_par = []
lista_num_impar = []

# Loop para inserção condicional de números

while num[-1] != 0: # enquanto o último elemento da lista num[] for diferente de zero faça
    n = int(input("Insira um número ou insira 0 para terminar o programa: ")) # peça um número inteiro
    num.append(n) # adicione o número inserido no final da lista (passa a ser o num[-1])

else: # se num[-1]==0 faça
    num.remove(num[0]) # remoção do primeiro elemento, que neste caso será sempre 1
    num.remove(num[-1]) # remoção do último elemento, que neste caso será sempre 0

# Filtrar lista e dividir atribuir a lista de pares, ímpares.  

for e in num:

    if e%2==0:
        lista_num_par.append(e)

    else:
        lista_num_impar.append(e)

# Mostrar resultados.

print("A soma dos números pares é",sum(lista_num_par))
print("A média aritmética dos números ímpares é",(sum(lista_num_impar)//len(lista_num_impar)))         

## Faça um programa que leia uma seqüência de números terminada por 0 e imprima o número que for múltiplo de sua posição na seqüência.

# Criar lista para conter números inseridos com um elemento diferente de zero

num = [1]

# Loop para inserção condicional de números

while num[-1] != 0: # enquanto o último elemento da lista num[] for diferente de zero faça
    n = int(input("Insira um número ou insira 0 para terminar o programa: ")) # peça um número inteiro
    num.append(n) # adicione o número inserido no final da lista (passa a ser o num[-1])

else: # se num[-1]==0 faça
    num.remove(num[0]) # remoção do primeiro elemento, que neste caso será sempre 1
    num.remove(num[-1]) # remoção do último elemento, que neste caso será sempre 0

# se o número da lista for múltiplo de sua posição na sequência imprima este numero

for e in num: # para cada elemento na lista faça
    if e%(num.index(e)+1)==0: # se o resto da divisão inteira do elemento pela posição dele for igual a zero
        print(e) # imprima este número
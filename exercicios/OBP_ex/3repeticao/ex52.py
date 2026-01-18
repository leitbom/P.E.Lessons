## Faça um programa que leia uma seqüência de números terminada por 0 e imprima o maior, o menor e a média aritmética dos números. 
## O número 0 (zero) não faz parte da seqüência.

# Criar lista para conter números inseridos com um elemento diferente de zero

num = [1]

# Loop para inserção condicional de números

while num[-1] != 0: # enquanto o último elemento da lista num[] for diferente de zero faça
    n = int(input("Insira um número ou insira 0 para terminar o programa: ")) # peça um número inteiro (se não quiser inteiro basta mudar classe)
    num.append(n) # adicione o número inserido no final da lista (passa a ser o num[-1])

else: # se num[-1]==0 faça
    num.remove(num[0]) # remoção do primeiro elemento, que neste caso será sempre 1
    num.remove(num[-1]) # remoção do último elemento, que neste caso será sempre 0

# Mostrar resultados desejados    

print("O maior número inserido foi",max(num)) # mostrar maior número
print("O menor número inserido foi",min(num)) # mostrar menor número
print("A média aritmética dos números lidos é",(sum(num))//len(num)) # mostrar soma dos números da lista dividido(se mudar classe deverá mudar o tipo de divisão) pelo tamanho da lista 

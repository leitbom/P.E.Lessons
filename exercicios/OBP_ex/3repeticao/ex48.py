## Faça um programa que leia um número da entrada (num), a seguir leia num números da entrada e os imprima.

num = int(input("Quantos números você deseja inserir? "))

lista_num = []

# Forçar o usuário a inserir um número inteiro positivo

while num<0:
    num = int(input("Quantos números você deseja inserir?(Insira um número inteiro positivo) "))

for n in range (num):
    numl = int(input("Insira um número inteiro: "))
    lista_num.append(numl)

# Para imprimir todos os números da lista na mesma linha    

for e in lista_num:
    print(e,end=" ")
    
# Tenho que melhorar minha forma de imprimir numeros na mesma linha
# Posso usar print nas listas mas sempre mostra aquelas malditas chaves 
# Entretanto se eu uso esse "método" da linha 19 não consigo usar separadores
# Talvez eu esteja pensando demais
# Se funciona eu deveria me preocupar com a aparência final? Isso não é preocupação do front-end?

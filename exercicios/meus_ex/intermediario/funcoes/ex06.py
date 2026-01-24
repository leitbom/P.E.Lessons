## Faça uma função que permita ao usuário inserir n números em uma lista
## Mostre uma lista1 com os números inseridos
## Mostre uma lista2 contendo os ímpares da lista 1
## Mostre uma lista3 contendo os pares da lista 1
## Mostre uma lista4 contendo os números primos da lista 1
## Mostre uma lista5 contendo os elementos da lista 1 em ordem crescente
## Mostre uma lista6 contendo os elementos da lista 1 em ordem decrescente

def multi_listas():
    def primo(num):
            if num <= 1:
                return False 
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False  
            return True
    print("="*75)
    n = int(input("Insira quantos elementos a lista original vai conter: "))
    print("="*75)
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    while n!=0:
        n -= 1
        num = int(input("Insira um elemento inteiro: "))
        print("="*75)
        lista1.append(num)
        if primo(num)==True:
            lista4.append(num)
        if num%2!=0:
            lista2.append(num)
        else:
            lista3.append(num)

    print ("Lista Original ==>",lista1)
    print("="*75)
    print ("Lista Ímpares ==>",lista2)
    print("="*75)
    print ("Lista Pares ==>",lista3)
    print("="*75)
    print ("Lista Primos ==>",lista4)
    print("="*75)
    print ("Lista Crescente ==>",sorted(lista1))
    print("="*75)
    print ("Lista Decrescente ==>",sorted(lista1,reverse=True))
    print("="*75)
multi_listas()

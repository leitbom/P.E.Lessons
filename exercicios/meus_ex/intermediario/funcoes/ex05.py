## Crie uma função que leia n numeros inteiros e
## *Crie uma lista1 contendo os números inseridos
## *Crie uma lista2 contendo os pares da lista1
## *Crie uma lista3 contendo os ímpares da lista1
## *Crie uma lista4 contendo os primos da lista1
## *Crie uma lista5 contendo os elementos da lista1 em ordem crescente
## *Crie uma lista6 contendo os elementos da lista1 em ordem decrescente
def listasex():
    
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    print("="*75)
    n = int(input("Quantos elementos a lista original deverá conter: "))
    print("="*75)
    
    while n != 0:
        n -= 1
        num = int(input("Insira um número inteiro: "))
        print("="*75)
        lista1.append(num)

        if num % 2 == 0:
            lista2.append(num)
        else:
            lista3.append(num)

    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    print(lista1.sort())
    print(lista1.sort(),reversed=True)
        
    
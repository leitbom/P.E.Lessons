###
## Faça um programa que permita o usuário inserir um número inteiro 
## Verifique se ele é primo e retorne uma mensagem ao utilizador

# Tive que pedir ajuda à IA pois meu cérebro estava derretendo...
# Deve funcionar bem para números grandes também....
# eu programa demorava muito para verificar números com mais de 10 casas decimais...

num = int(input("Digite um número: "))

if num <= 1:
    print("Não é primo")
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        print("É primo")
    else:
        print("Não é primo")




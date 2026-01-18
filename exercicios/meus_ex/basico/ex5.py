## Faça um programa que leia dois números e imprima uma mensagem dizendo qual deles é o maior. ##
## Se os números forem iguais, imprima uma mensagem avisando o usuário. ##

num_1 = float(input("Atribua um valor para o primeiro número: "))
num_2 = float(input("Atribua um valor para o segundo número: "))

if num_1 == num_2:

    print("="*50)
    print("Os números são iguais.")
    print("="*50)

else:
    if num_1 > num_2:

        print("="*50)
        print("O maior número é ", num_1)
        print("="*50)
    else:
        
        print("="*50)
        print("O maior número é ", num_2)
        print("="*50)

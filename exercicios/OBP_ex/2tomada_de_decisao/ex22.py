## Faça um programa que leia a idade de uma pessoa e informe sua classe eleitoral:
## · não eleitor (abaixo de 16 anos);
## · eleitor obrigatório (entre 18 e 65 anos);
## · eleitor facultativo (entre 16 e 18 anos e acima dos 65 anos).

idade = int(input("Insira a idade: "))

while idade < 0:
    idade = int(input("Insira uma idade válida: "))

if idade < 16:
    print("Não eleitor")

elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")

elif idade >= 16 and idade < 18 or idade > 65:
    print("Eleitor facultativo")

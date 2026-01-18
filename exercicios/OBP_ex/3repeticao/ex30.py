## Faça um programa que leia um número da entrada e imprima os números naturais de 0 até este número, pulando de dois em dois. 
## Suponha que o número lido da entrada será maior que zero.


num = int(input("Insira um número maior que zero: "))

# Novamente forçando o usuário a inserir um número desejado...

while num <= 0:
    num = int(input("Insira um número maior que zero: "))

for n in range(0,num+1,2):
    print(n)

# Talvez o enunciado seja dúbio?
# "até este número" não implicaria que este numero teria que aparecer no final?
# Neste caso o aprimoramento do código requer uma condicional para o num inserido se for par ou ímpar.

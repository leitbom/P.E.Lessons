## (Prova 1 - 96/1) Faça um programa que imprima a tabela de conversão de graus Celsius-Fahrenheit para o intervalo desejado pelo usuário. 
## O programa deve solicitar ao usuário o limite superior, o limite inferior do intervalo e o decremento.
## Fórmula de conversão: C = 5*(F - 32)/9  
## Exemplo:  valores lidos: 68 50 15 
##          impressão:  Fahrenheit     Celsius 
##                      68             20 
##                      53             11


flims = float(input("Insira o limite superior: "))
flimi = float(input("Insira o limite inferior: "))
fdecr = float(input("Insira um valor para um decremento: "))

# É só subrair o decr do flims 
# C = 5*(F - 32)//9
# f'{x:.yf}' ==> x é o que eu quero formatar (y é a quantidade de casas decimais, tem que ser um int)

print("Fahrenheit     Celsius")

while flims > flimi:
    print(f'{flims:.2f}',f'{5*(flims-32)/9:.2f}',sep="           ",end="\n")
    flims -= fdecr

# Tá tabelado essa merda...

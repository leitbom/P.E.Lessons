## (Prova 1 - 96/2) Uma telenovela de grande sucesso tem o seu final previsto para o dia 1 o de novembro.
## Sabe-se que neste dia será revelado nome do personagem responsável por inúmeros assassinatos ocorridos no decorrer da trama.
## No entanto, no dia 1 o de outubro (um mês antes do término da novela), um funcionário da emissora conta para dois amigos o desfecho do último capítulo.
## Com isto, no dia 1 de outubro, 3 pessoas sabem do desfecho da novela.
## Supondo que cada nova pessoa a saber do final da novela contará para duas novas pessoas no dia seguinte (e para mais ninguém), mais 4 pessoas estarão envolvidas ao final do dia 2 de outubro (7 pessoas até este dia).
## No dia 3 de outubro, já serão 15 pessoas.
## Faça um programa para ajudar o dono da emissora a decidir se deve demitir o funcionário fofoqueiro: se ao término do dia 25 de outubro mais de 20000 (vinte  mil) pessoas estiverem sabendo do final da novela, o funcionário deverá ser demitido.

# Total de pessoas que sabem:   1==>3==>7==>15...
# Aumento de pessoas por dia:   1=>+2=>+4=>+08...
# Dias:                         1==>1==>2==>03...

lista_fofoca = [1,2,4,8,15] ## elemento 0 e 1 são considerados para o dia 01/10, logo essa lista corresponde a 4 dias
contador = 4

# O último elemento da lista é sempre o total de pessoas que sabem 

while contador != 25:
    contador += 1 # adiciona 1 dia ao contador com limite 25
    lista_fofoca.append(sum(lista_fofoca)) # adiciona a soma dos elementos da lista como um novo elemento ao final da lista
    
    if lista_fofoca[-1] > 20000: # condicional dentro do loop se o último elemento for maior que limite(20k) printar mensagem e break loop
        print("="*100)  
        print("Demita!")
        print("="*100)
        break

if lista_fofoca[-1] <= 20000: # condicional fora do loop de correr os 25 dias e não ultrapassar limite(20k) printar mensagem
    print("="*100)  
    print("Não demita!")
    print("="*100)

# Mensagem mostrando resultados ao dono da emissora com projeções

print("No dia",contador, "as projeções indicam que",sum(lista_fofoca), "pessoas vão saber do desfecho da novela")
print("="*100)

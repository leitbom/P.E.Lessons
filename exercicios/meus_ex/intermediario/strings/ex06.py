## Faça um programa que leia uma data de nascimento (DD/MM/AAAA)
## Imprima a data com o nome do mês por extenso

meses= {1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"}

dia = int(input("Insira seu dia de nascimento: "))
mes = int(input("Insira seu mês de nascimento: "))
ano = int(input("Insira seu ano de nascimento: "))

while dia not in range(1,32) or mes not in range(1,13) or ano > 2026:
    print("Insira uma data válida!")
    dia = int(input("Insira seu dia de nascimento: "))
    mes = int(input("Insira seu mês de nascimento: "))
    ano = int(input("Insira seu ano de nascimento: "))

if mes in meses:
    mes = meses[mes]

print("Você nasceu em",dia,"de",mes,"de",ano)

# Que lindo...to orgulhoso de mim...
# Ainda dá pra melhorar o input da data para não ser input separado...

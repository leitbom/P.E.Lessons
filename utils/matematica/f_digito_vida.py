## Este programa serve para pedir uma data de nascimento.
## Verificar validade e fazer somas sucessivas até chegar ao algarismo popularmente conhecido como Dígito da Vida.

# Preciso otimizar esse programa...

def digito_vida():
    datadia =int(input("Insira seu dia de nascimento formato DD: "))
    datames =int(input("Insira seu mês de nascimento formato MM: "))
    dataano =int(input("Insira seu ano de nascimento formato AAAA: "))

    # lista contendo dia, mês e ano de nascimento
    datanasc = [datadia, datames, dataano] 

    # Declarar variáveis de somas
    # Sempre se fará necessário fazer duas somar separadas, uma para os elementos e uma para os 4 algarismos da variável

    soma = 0
    somafinal = 0

    # Prender usuário em loop para inserir data válida no intervalo (01/01/1990 - 31/12/2026)

    while datanasc[0]<1 or datanasc[0]>31 or datanasc[1]<1 or datanasc[1]>12 or datanasc[2]<1900 or datanasc[2]>2026:
        print("Insira uma data válida")
        datadia =int(input("Insira seu dia de nascimento formato DD: "))
        datames =int(input("Insira seu mês de nascimento formato MM: "))
        dataano =int(input("Insira seu ano de nascimento formato AA: "))
        datanasc = [datadia, datames, dataano]

    # Somar elementos da lista

    for ele in datanasc:
        soma += ele

    # Somar elementos da variável soma

    while soma > 0:
        resto = soma % 10
        soma = soma // 10
        somafinal += resto

    # Resultado

    return "Seu dígito da vida é...", somafinal

mensagem, variavel = digito_vida()
print(mensagem, variavel)

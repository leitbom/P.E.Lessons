## Este programa serve para dar dois inputs e verificar se as strings são anagramas entre si.
## Independentemente se são maiúsculas ou minúsculas.

# Necessita revisão...

# Função anagrama entre 2 strings

def anagrama():

    # Pedir string
    # Modificar e guardar em variável
    # Criar variável de contagem por texto

    texto = str(input("Insira um texto para verificação: "))
    texto = texto.replace(" ", "")
    maius = texto.upper()
    soma = 0

    # Pedir string
    # Modificar e guardar em variável
    # Criar variável de contagem por texto

    texto2 = str(input("Insira um texto para verificação: "))
    texto2 = texto2.replace(" ", "")
    maius2 = texto2.upper()
    soma2 = 0

    # Criar loop que prende o usuario para ele não inserir strings vazias

    while texto =="" or texto2 =="":
        texto = str(input("Insira um texto para verificação: "))
        texto = texto.replace(" ", "")
        maius = texto.upper()
        texto2 = str(input("Insira um texto para verificação: "))
        texto2 = texto2.replace(" ", "")
        maius2 = texto2.upper()

    # Por letra no texto some ao primeiro contador o valor de ordem do caractere

    for i in maius:
        soma += ord(i)

    # Por letra no texto some ao segundo contador o valor de ordem do caractere

    for j in maius2:
        soma2 += ord(j)

    # Usar if/else para verificar se é anagrama

    if soma == soma2:
        return True, "É um anagrama"

    else:
        return False, "Não é um anagrama"
    
resultado, mensagem = anagrama()
print(mensagem)

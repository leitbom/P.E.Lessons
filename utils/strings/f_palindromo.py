## Este programa serve para verificar se uma string insrida é ou não um palíndromo

# Função palíndromo

def palindromo():

    # Pedir input de string
    # Realizar modificações na string com methods .replace() ==> (para ignorar espaços) e .upper() ==> (para ignorar a diferença de caixas)
    # Guardar modificações em variável nova

    texto = str(input("Insira um texto para verificação: "))
    texto = texto.replace(" ", "")
    maius = texto.upper()
    inverso = maius[::-1]

    # Prender usuário em loop que evita input de strings vazias e cause falsos resultados

    while texto == "":
        print("é uma string vazia, não é um palindromo!")
        texto = str(input("Insira um texto para verificação, que não seja vazio: "))
        texto = texto.replace(" ", "")
        maius = texto.upper()
        inverso = maius[::-1]

    # Verificação de palindromo com if/else
    
    if maius == inverso:
        return True, "É um palíndromo!"

    else:
        return False, "Não é um palindromo!"

resultado, mensagem = palindromo()
print(mensagem)

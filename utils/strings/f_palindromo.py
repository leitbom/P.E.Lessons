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

    # Se a string for vazia

    if texto == "":
        return False, "É uma string vazia, não é um palíndromo!"

    # Verificação de palindromo com if/else
    
    if maius == inverso:
        return True, "É um palíndromo!"

    else:
        return False, "Não é um palindromo!"

resultado, mensagem = palindromo()
print(mensagem)

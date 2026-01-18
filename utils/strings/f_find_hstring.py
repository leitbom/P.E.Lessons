## Escrever um programa que lê duas strings e verifica se a primeira está contida na segunda 

# função find hidden string in string

def find_hstr():

# Recebe dois inputs

    string1 = (input("Escreva uma palavra: ")).strip()
    string2 = (input("Escreva um texto: ")).strip()

# Recebe um contador para percorrer a primeira string

    contador = 0

# Percorre a segunda string
# Se a letra atual da segunda string correspode à letra atual da primeira string 
# O contador serve para avançar para a próxima letra da primeira string

    for letter in string2:
        if contador < len(string1) and letter == string1[contador]:
            contador += 1

# Se percorrer a primeira string, significa que está contida

    if contador == len(string1):
        return True, "Resultado positivo."
    
    else:
        return False, "Resultado negativo."
    
resultado, mensagem = find_hstr()
print(mensagem)

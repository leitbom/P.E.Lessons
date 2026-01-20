## Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
## *Quantos espaços em branco existem na frase.
## *Quantas vezes aparecem as vogais a, e, i, o, u.

texto = str(input("Insira um texto: ")) # input de string
vogais = "aáàâãeéêiíoóõôuúAÁÀÂÃEÉÊIÍOÓÕÔUÚ" # string contendo vogais minúsculas e maiúsculas e suas possíveis acentuações
blank = " " # string contendo 1 espaço em branco
for char in texto: # por cada charactere em texto
    for vog in vogais: # por cada vogal em vogais
        if char == vog: # se caractere for igual a vogal
            cvogais += 1 # contador de vogais +1

        
print(texto.count(blank)) # conta os espaços brancos 
print(cvogais) # mostra o contador de vogais

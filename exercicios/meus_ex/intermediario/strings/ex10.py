## Faça um programa que utilize uma lista contendo 10 palavras
## Faça uma escolha aleatória de uma dessas palavras 
## O usuário possa inserir uma string para tentar adivinhar qual é a palavra
## O usuário seja avisado de quantas letras ele acertou a cada tentativa

import random
p = ["python","anaconda","jupyther","ghostwritter","pagenotfound","error","syntax","exercices","pylovers","gamedev"]
psecreta = random.choice(p)
print("="*75)
print("A palavra secreta possui",len(psecreta),"letras")
print("="*75)


while True:
    palavra = str(input("Try again..."))
    if psecreta != palavra:
        for letra in psecreta:
            for l in palavra:
                if letra == l:
                    print("A palavra contem a/as letras",l)
        continue
    else:
        print("Congratulations")
        break
    
# tá meio estranho

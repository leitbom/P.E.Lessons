## Do a program that uses a list containing 10 words
## Do a random choice of one of these words
## The user can enter a string to try to guess the word 
## The user is informed of how many letters he got right each attempt
## Faça um programa que utilize uma lista contendo 10 palavras
## Faça uma escolha aleatória de uma dessas palavras 
## O usuário possa inserir uma string para tentar adivinhar qual é a palavra
## O usuário seja avisado de quantas letras ele acertou a cada tentativa

try:
    import random
    p = ["python","anaconda","jupyther","ghostwritter","pagenotfound","error","syntax","exercices","pylovers","gamedev"]
    psecreta = random.choice(p)
    print("="*75)
    print("The secret word has",len(psecreta),"letters.")
    print("="*75)


    while True:
        palavra = str(input("Try a word..."))
        if psecreta != palavra:
            for letra in psecreta:
                for l in palavra:
                    if letra == l:
                        print("The word contains the letter",l)
            continue
        else:
            print("Congratulations")
            break
except:
    print("Something went wrong.")

# its a bit weird
# tá meio estranho

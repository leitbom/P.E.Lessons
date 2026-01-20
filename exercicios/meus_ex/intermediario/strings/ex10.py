## Faça um programa jogo da forca em que o jogador terá 6 chances de descobrir a palavra
## Utilize um dicionário contendo as possíveis palavras e o módulo random para uma escolha aleatória

l = ["palavra","coisas","trabalho","retorno","zebra","aulas","fugaz"]

from random import choice

palavras = choice(l)
print(palavras)
lpal1 = []
lpal2 = []
lpal = [lpal1,lpal2]

for char in palavras:
    lpal1.append(char)

for n in range(5):
    print(lpal2)
    letra = str(input("Insira uma letra: "))
    
    if letra in lpal1:
        lpal2.append(letra)
    else:
        print("não contém essa letra")


# my brain... starting to melt... why so hard mommy?
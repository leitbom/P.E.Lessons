## Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
## *Quantos espaços em branco existem na frase.
## *Quantas vezes aparecem as vogais a, e, i, o, u.

fteste = "filhos de uma mãe santa"
vogais = "aeiouAEIOU"
blank = " "
cvogais = 0
for char in vogais:
    if char in fteste:
        cvogais += 1
print(fteste.count(blank))
print(cvogais)
# not finished yet, going to work...
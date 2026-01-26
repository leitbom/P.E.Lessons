## Do a program that reads a string with a phrase entered by the user (including spaces), count:
## *How many blank spaces are in the sentence.
## *How many times the vowels a, e, i, o, u appear.
## Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
## *Quantos espaços em branco existem na frase.
## *Quantas vezes aparecem as vogais a, e, i, o, u.

try:
    texto = str(input("Enter a string: ")) # input string from user
    vogais = "aáàâãeéêiíoóõôuúAÁÀÂÃEÉÊIÍOÓÕÔUÚ" # string with all vowels
    blank = " " # string containing 1 white space
    cvogais = 0 # vowel counter initialized to 0
    for char in texto: # for each character in text
        for vog in vogais: # for each vowel in vowels
            if char == vog: 
                cvogais += 1 # vowel counter +1
except:
    print("Something went wrong.")
else:      
    print(texto.count(blank)) # count white spaces in the string
    print(cvogais) # show vowels counter

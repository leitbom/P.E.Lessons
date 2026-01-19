## Faça um programa que leia uma string.
## Imprima a string em formato de escada.

texto = str(input("Insira uma string: "))
txt = ""

for char in texto:
    txt += char
    print(txt)

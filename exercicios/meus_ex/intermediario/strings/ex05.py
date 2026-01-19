## Faça um programa que leia uma string.
## Imprima a string em formato de escada invertida.

texto = str(input("Insira uma string: "))
print(texto)

for char in texto:
    texto = texto[:-1]
    print(texto)

## Do a program that reads two strings.
## Print them on the screen.
## Inform the number of characters and whether they have the same length or not.
## If they have the same content or not.
## Faça um programa que leia duas strings.
## Printe elas na tela.
## Informe a quantidade de caracteres e se elas tem o mesmo tamanho ou não.
## Se elas possuem o mesmo conteúdo ou não.
try:
    pal1 = str(input("Enter a string: "))
    pal2 = str(input("Enter a string: "))

    print("The length of",pal1,":",len(pal1),"characters")
    print("The length of",pal2,":",len(pal2),"characters")

    # Verificar se têm o mesmo tamanho
    if len(pal1) != len(pal2):
        print("Both strings have different lengths.")

    else:
        print("Both strings have the same length.")

    # Verificar se têm o mesmo conteúdo
    if pal1 == pal2:
        print("The content of the strings are equal.")

    else:
        print("The content of the strings are different.")
except KeyboardInterrupt:
    print("You've interrupted the program.")
except:
    print("An error occurred. Please try again.")

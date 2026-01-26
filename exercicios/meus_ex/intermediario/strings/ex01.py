## Faça um programa que leia duas strings.
## Printe elas na tela.
## Informe a quantidade de caracteres e se elas tem o mesmo tamanho ou não.
## Se elas possuem o mesmo conteúdo ou não.
try:
    pal1 = str(input("Insira um texto: "))
    pal2 = str(input("Insira um texto: "))

    print("O tamanho de",pal1,":",len(pal1),"caracteres")
    print("O tamanho d()",pal2,":",len(pal2),"caracteres")

    # Verificar se têm o mesmo tamanho
    if len(pal1) != len(pal2):
        print("As duas strings possuem tamanhos diferentes.")

    else:
        print("As duas strings possuem o mesmo tamanho")

    # Verificar se têm o mesmo conteúdo
    if pal1 == pal2:
        print("O conteúdo das strings são iguais.")

    else:
        print("O conteúdo das strings são diferentes.")
except KeyboardInterrupt:
    print("You've interrupted the program.")
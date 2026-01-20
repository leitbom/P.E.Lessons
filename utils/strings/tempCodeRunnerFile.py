    texto = str(input("Insira uma string:")) # input de string
    texto = texto.upper() # manipulação para ignorar diferença de caixa

    for char in texto: # para cada caractere na string
        if char.isupper()==True: # se for caixa alta continue o loop
            continue
        else: # se não troque o caractere por ""
            texto = texto.replace(char,"")
    while texto == "": # enquanto string for vazia retorne False e saia do loop
        print(False)
        break  
    else:  # se não for vazia
        if texto == texto[::-1]: # se for palíndromo retorne True
            print(True)
        else: # se não retorne False
            print(False)
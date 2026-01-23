## Crie uma função que execute um timer em que o usuário insere horas, minutos e segundos
## É permitido importação do módulo time para realizar a contagem 

# importar time
# usuario insere hora em inteiro
# usuario insere minuto em inteiro
# usuário insere segundos em inteiro
# contador = int((segundos) + (minutos*60) + (horas*(60**2))) ==> isso nos dá o total de segundos
# programa faz contagem regressiva segundo a segundo subtraindo do contador
# while contador != 0
    # time.sleep(1) 
    # print(contador-1)
# else:
    # return "O tempo acabou!"
def timer():
    import time
    hora = int(input("Insira uma hora: "))
    minuto = int(input("Insira um minutos: "))
    segundo = int(input("Insira um segundo: "))
    timer = int(segundo)+(minuto*60)+(hora*(60**2))
    print(timer, "segundos restantes")

    while timer!=0:
        time.sleep(1)
        timer -= 1
        return (timer,"segundos restantes")
    else:
        return("Fim do timer...acorda cara!")  

# Esse programa realiza a tarefa mas não mostra o display de timer...
# Bom pelo menos ele faz a tarefa...display é meu ovo

## Do a function that execute a timer wich the user input hours, minutes and seconds.
## It's permited the import of time module to make the countdown.
## Crie uma função que execute um timer em que o usuário insere horas, minutos e segundos.
## É permitido importação do módulo time para realizar a contagem.

def timer():
    try:
        import time # import time
        hora = int(input("Enter hours: ")) # user enter an hour (interger number).
        minuto = int(input("Enter minutes: ")) # user enter a minute (interger number).
        segundo = int(input("Enter seconds: ")) # user enter a second (interger number).
        timer = segundo+(minuto*60)+(hora*(60**2)) # contador = segundos + (minutos*60) + (horas*(60**2))) ==> total of seconds.
    except:
        print("You've done something wrong.")
    else:
        print(timer, "seconds left") # total remaining seconds.
        while timer!=0:
            time.sleep(1)
            timer -= 1 # program do a regressive countdown second to second, counter = counter -1.
            print(timer,"seconds left")
        print("Wake up dude!") 
timer()

# This program does not show a display of hours, minutes and seconds like (hh:mm:ss).
# It only count seconds.
# Later I could improve this code, but I'm lazy.

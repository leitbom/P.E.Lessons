## Do a program that reads a birth date (DD/MM/YYYY)
## Print the date with the month name in full.
## Faça um programa que leia uma data de nascimento (DD/MM/AAAA)
## Imprima a data com o nome do mês por extenso

try:
    meses= {1: "january",
            2: "february",
            3: "march",
            4: "april",
            5: "may",
            6: "june",
            7: "july",
            8: "august",
            9: "september",
            10: "october",
            11: "november",
            12: "december"}
    dia = int(input("Enter your birth day: "))
    mes = int(input("Enter your birth month: "))
    ano = int(input("Enter your birth year: "))
    while dia not in range(1,32) or mes not in range(1,13) or ano > 2026:
        print("Enter a valid date!")
        dia = int(input("Enter your birth day: "))
        mes = int(input("Enter your birth month: "))
        ano = int(input("Enter your birth year: "))
    if mes in meses:
        mes = meses[mes]
except KeyboardInterrupt:
    print("You interrupted the program.")
except ValueError:
    print("Invalid input. Please enter numeric values for day, month, and year.")
except:
    print("An unexpected error occurred.")
else:
    print("You were born on",dia,"of",mes,"of",ano)

# What a beautiful code...I'm proud of myself...
# Ain't it better to improve the date input to not be separate inputs...
# Que lindo...to orgulhoso de mim...
# Ainda dá pra melhorar o input da data para não ser input separado...

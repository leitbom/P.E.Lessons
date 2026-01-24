## Faça uma função que peça dois números inteiros e faça a divisão real do primeiro pelo segundo.
## Utilize try/exept para tentar blindar o código de possíveis inputs indesejáveis

def float_div_2ints():
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        division = first_number / second_number
    except ValueError:
        print("Type not valid.")
    except ZeroDivisionError:
        print("Can not divide by zero. Run again baby.")
    else:
        print(division)

float_div_2ints()

# Esse exercício foi muito bom, aprendi bastante! E ainda consegui fazer em inglês
# Agora eu vejo um pouco de toda a merda que eu estava fazendo, tá tudo tão feio agora...
# Indo dormir depois dessa
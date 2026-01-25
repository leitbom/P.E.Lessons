## Do a function wich takes a nunber as input and print if it's a perfect square.
## Remember that perfect squares are numbers wich have an integer square root.
## Faça uma função capaz de ler um número e dizer se é um quadrado perfeito.
## Lembre-se que quadrados perfeitos são números que possuem raiz quadrada inteira.

def perfect_sqr_num():
    try:
        num = int(input("Enter a positive integer number: "))
        if num == 0 or num//num**(1/2) == num**(1/2):
            print("It's a perfect square.")
    except:
        print("You've done something wrong.")                     
perfect_sqr_num()

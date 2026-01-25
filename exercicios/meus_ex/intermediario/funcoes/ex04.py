## Do a function wich verify if an inputed number is.
## It's even or odd.
## It's prime or not.
## Print the results.
## Crie uma função que verifique se um número inserido é
## É par ou ímpar
## É primo ou não
## Mostre na tela os resultados.

def nipp():
    try:
        print("="*50)
        num = int(input("Enter an integer number: "))
        print("="*50)
        def par_impar():
            if num%2==0:
                print("It's even.")
                print("="*50)
            else:
                print("It's odd." )
                print("="*50) 
        def primo(): # exercicios > meus_ex > basico > ex01.py 
            if num <= 1:
                print("Not prime")
            else:
                primo = True
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        primo = False
                        break
                if primo:
                    print("Prime")
                else:
                    print("Not prime")
    except:
        print("You've done something wrong.")
    else:
        return primo(),par_impar()    
nipp()

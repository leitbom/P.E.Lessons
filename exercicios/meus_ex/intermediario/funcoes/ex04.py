## Crie uma função que verifique se um número inserido 
## É par ou ímpar
## É primo ou não
## Mostre na tela os resultados na mesma linha

def nipp():
    num = int(input("Insira um número: "))
    def primo(num):
        if num <= 1:
            print("Número inválido para verificação de primo.")
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Não é primo.")
        print("É primo.")
    mp = primo(num)

    def par_impar():
        if num%2==0:
            print("É par.")
        else:
            print("É ímpar." )  
    mpi = par_impar()

    return mp,mpi
    
nipp()

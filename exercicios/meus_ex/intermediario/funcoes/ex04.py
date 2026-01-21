## Crie uma função que verifique se um número inserido 
## É par ou ímpar
## É primo ou não
## Mostre na tela os resultados na mesma linha


# dá pra por as duas dentro da mesma função??? ou exta função se chama módulo ex04.py??
# estou um pouco confuso...

num = int(input("Insira um número: "))
def primo():
    if num <= 1:
        return "Número inválido para verificação de primo."
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Não é primo."  
    return "É primo."
mp = primo()

def par_impar():
    if num%2==0:
        return "É par."
    else:
        return "É ímpar."   
mpi = par_impar()

print(mp,mpi)

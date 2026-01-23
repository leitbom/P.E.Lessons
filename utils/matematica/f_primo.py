def primo():
    num = int(input("Digite um número: "))

    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

print(primo()) # se for importar essa função delete esta linha 

# Caso a função seja invocada talvez seja necessário deletar a segunda linha para um uso somente de verificação
def primo():
    num = int(input("Digite um número: "))

    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

print(primo()) # se for inportar essa função delete esta linha
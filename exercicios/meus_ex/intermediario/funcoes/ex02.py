# Faça uma função capaz de ler um número e dizer se é um quadrado perfeito
# Lembre-se que quadrados perfeitos são números que possuem raiz quadrada inteira

def perfect_sqr_num():
    num = int(input("Insira um número inteiro: "))
   
    if num == 0:
        return False, "Número inserido é inválido..."
    elif num<0:
        return False, "O número não é um quadrado perfeito!"
    elif num//num**(1/2) == num**(1/2):
        return True, "O número é um quadrado perfeito!"
    else:
        return False, "O número não é um quadrado perfeito!"
    
resultado, mensagem = perfect_sqr_num()
print(mensagem)


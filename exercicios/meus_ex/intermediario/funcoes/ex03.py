## Crie uma função capaz de ler uma string e um número inseridos pelo usuário
## A função deve retornar a concatenação e interpolação da string com o número

def numstr_plus_x():
    text = str(input("Insira uma string: "))
    num = int(input("Insira um número inteiro:"))
    concat = text + str(num)
    interp = text * num
    if num <= 0:
        return "Concatenação ==>",concat,"A interpolação não é possível com números negativos","."
    else:
        return "Concatenação ==>",concat,"Interpolação ==>",interp

m1,m2,m3,m4 = numstr_plus_x()
print(m1,m2)
print(m3,m4)
    


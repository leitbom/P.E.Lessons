## Crie uma função capaz de diferenciar os tipos de um input
## E retorne apenas o tipo

def tipo(num):
    print(type(num).__name__)

# Testando
tipo(5)            
tipo("texto")     
tipo([1, 2, 3])   
tipo(3.14)       

# o input deve ser passado como parâmetro na invocação da função tipo()
## Do a function that can tell the type of an input.
## Must return only the type.
## Crie uma função capaz de diferenciar os tipos de um input.
## E retorne apenas o tipo.

def tipo(n):
    print(type(n).__name__)

# Tests
tipo(5)            
tipo("texto")     
tipo([1, 2, 3])   
tipo(3.14)  

# The input must be the paremeter in tipo() when it's called.
# Otherwise the function may look too big for a simple task.
# I know...I'm lazy XD
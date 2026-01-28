## Do a function that resolves a quadratic function.
## ax**2 + bx + c = 0
## The program must take a, b and c as inputs and gives the results x' and x" of the equation.
## Faça uma função que resolva uma função do segundo grau.
## ax**2 + bx + c = 0
## O programa deve receber a, b e c como inputs e retornar os resultados x' e x" da equação.

a = float(input("Enter the 'a' value: "))
b = float(input("Enter the 'b' value: "))
c = float(input("Enter the 'c' value: "))

from math import sqrt as rq

delta = b**2 - (4 * a * c)
if delta >= 0:
    rqdelta = rq(delta)
    x1 = (-b + rqdelta)/2*a
    x2 = (-b - rqdelta)/2*a
else:
    rqdelta = rq((-delta))
    x1 = str((-b + rqdelta)/2*a) + "+i"
    x2 = str((-b - rqdelta)/2*a) + "-i"

print(x1)
print(x2)

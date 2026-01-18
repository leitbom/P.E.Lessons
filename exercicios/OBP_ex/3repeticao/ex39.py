## Faça um programa que imprima a soma dos números pares entre 25 e 100.
somatorio = 0
for n in range(25,101):
    if n % 2 == 0:
        somatorio += n 

print("Somatório dos pares entre 25 e 100 = ", somatorio)

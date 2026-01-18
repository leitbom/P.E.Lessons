###
## Faça um programa que calcule o M.M.C. entre dois números lidos da entrada.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 == 0 and num2 == 0:
    print("MMC = 0")
else:
    a, b = abs(num1), abs(num2)
    original_a, original_b = a, b
    
    while b != 0:
        a, b = b, a % b
    
    mdc = a
    mmc = (original_a * original_b) // mdc
    
    print("MMC =", mmc)
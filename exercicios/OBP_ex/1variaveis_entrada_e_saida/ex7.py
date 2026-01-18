## Faça um programa que leia um valor de conta de restaurante, representando o gasto realizado pelo cliente e imprima o valor total a ser pago, considerando que o restaurante cobra 10% para o garçom.

conta = float(input("Insira o valor da conta do cliente x : "))
gar = conta/10
print("="*50)
print("O valor da conta é de ", conta)
print("="*50)
print("O valor de serviço do garçom é de ", gar)
print("="*50)
print("O valor total da sua conta é de ", conta+gar)


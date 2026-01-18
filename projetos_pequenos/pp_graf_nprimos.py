###
## Crie um programa que faça um gráfico simples contendo n pontos e os segmentos de reta que os unem consecutivamente
## Eixos marcam a posição do número primo. Exemplo: a(1,2), b(2,3), c(3,5), d(4,7)....
## x para posição e y para o valor


n = int(input("Insira a quantidade de números primos consecutivos que deseja ver no gráfico: "))

import matplotlib.pyplot as plt

# Encontrar os n primeiros números primos
primos = []
num = 2
while len(primos) < n:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        primos.append(num)
    num += 1
# Até aqui ok...e agora?


# Criar gráfico
plt.figure(figsize=(10, 5))
plt.plot(range(1, n+1), primos, 'b-o', linewidth=2, markersize=6)
plt.title('100 Primeiros Números Primos')
plt.xlabel('Posição')
plt.ylabel('Valor do primo')
plt.grid(True, alpha=0.3)
plt.show()

# Isso eu n ia fazer tão cedo...vlw dona IA

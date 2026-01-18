## Faça um programa que leia um horário no sistema de 24 horas e imprima este horário no sistema de 12 horas.

# Como ainda não sei mexer muito bem com essa questão de formatação.
# Escolhi por dividir o programa para lidar separadamente com horas e minutos.
# Pode não parecer muito prático, mas funcionou bem para mim...

horas = int(input("Indique as horas: "))
minutos = int(input("Indique os minutos: "))

# Loop que prende o usuário afim de inserir um horário válido.
# Sem horas fora de (0 - 23) e sem horas negativas.
# Sem minutos fora de (0 - 59) e sem minutos negativos.

while horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    
    horas = int(input("Indique as horas: "))
    minutos = int(input("Indique os minutos: "))

# Escolhi guardar os valores em uma lista, pq assim posso modificar os elementos se assim eu quiser.

horario24 = [horas,":", minutos]

# Condicionais

if horas < 12 and horas >= 0: #de 0 - 11 é am

    if horas - 12 < 0:
        horario12 = [horas, ":", minutos, "am"]

elif horas >=12 and horas <=23: #de 12 - 23 é pm
        
    horario12 = [horas-12, ":", minutos, "pm"]

# Loop para print no formato desejado

for e in horario12:
    print(e, end=" ")

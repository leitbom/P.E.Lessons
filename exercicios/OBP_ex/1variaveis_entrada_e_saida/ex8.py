## Faça um programa que leia um valor de hora e informe quantos minutos se passaram deste o início do dia.

print("="*50)
horas = int(input("Informe as horas: ")) 
print("="*50)
minutos = int(input("Informe os minutos: ")) 
print("="*50)

while horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    print("Informe um horário válido")
    print("="*50)
    horas = int(input("Informe as horas: ")) 
    print("="*50)
    minutos = int(input("Informe os minutos: ")) 
    print("="*50)

minuto_final = horas*60 + minutos

print("Se passaram", minuto_final, "minutos desde o início do dia.")
print("="*50)
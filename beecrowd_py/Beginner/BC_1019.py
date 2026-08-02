#Resolução do exercicio BC 1019 - Conversão do horario

#Entrada de dados

sec = int(input())
horas = 0
minutos = 0
segundos = 0

#processamento de dados 

while sec > 0:
    if sec >= 3600:
        horas = horas + 1
        sec -= 3600
    elif sec >= 60:
        minutos = minutos + 1
        sec -= 60
    elif sec >= 1:
        segundos = segundos +1
        sec -= 1

#Saída de dados

print(f'{horas}:{minutos}:{segundos}')
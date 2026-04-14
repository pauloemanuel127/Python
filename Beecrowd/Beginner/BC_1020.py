#Resolução do exercicio BC 1020 - idade em dias

#entrada de dados

in_days = int(input())
years = 0
months = 0

#processamento de dados

while in_days > 29:
    if in_days >= 365:
        years += 1
        in_days -= 365
    elif in_days >= 30:
        months += 1
        in_days -= 30

#Saída de dados

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{in_days} dia(s)')
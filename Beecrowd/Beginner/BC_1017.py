#Resolução do exercicio BC 1017 - combustivel gasto

#Entrada de dados

horas = int(input())
velocidade = int(input())

#Processamento de dados

distancia = horas*velocidade
litros = distancia/12

#Saída de dados

print(f'{litros:.3f}')
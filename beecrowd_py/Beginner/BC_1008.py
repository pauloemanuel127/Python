#Resolução do exercicio BC 1008 - Salário

#Entrada de dados

number = int(input())
horas = int(input())
valor = float(input())

#Processamento dos dados 

salary = horas*valor

#Saída dos dados

print('NUMBER =', number)
print(f'SALARY = U$ {salary:.2f}')
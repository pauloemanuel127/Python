#Resolução do exercicio BC 1013 -  O maior

#Entrada de dados

numbs = input().split()

#processamento dos dados

num1 = int(numbs[0])
num2 = int(numbs[1])
num3 = int(numbs[2])

maior1 = (num1 + num2 + abs(num1 - num2))/2
maior2 = (maior1 + num3 + abs(maior1 - num3))/2

#Saída de dados

print(f'{maior2:.0f} eh o maior')
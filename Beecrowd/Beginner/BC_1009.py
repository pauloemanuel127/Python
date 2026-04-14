#Resolução do exercicio BC 1009 - Salário com bonus

#Entrada de dados

nome = input()
salario = float(input())
vendas = float(input())

#Processamento de dados  

bonus = (vendas*0.15)
total = salario+bonus

#Saída

print(f'TOTAL = R$ {total:.2f}')
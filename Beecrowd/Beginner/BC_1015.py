#Resolução do exercicio BC 1015 - Distancia entre dois pontos

#Entrada de dados

x1y1 = input().split()
x2y2 = input().split()

#Processamento de dados

x1 = float(x1y1[0])
y1 = float(x1y1[1])
x2 = float(x2y2[0])
y2 = float(x2y2[1])

resultado = (((x2-x1)**2)+(y2-y1)**2)**0.5

#Saída de dados

print(f'{resultado:.4f}')
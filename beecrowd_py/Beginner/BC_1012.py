#Resolução do exercicio BC 1012 - Area

#Dados base

pi = 3.14159

#Entrada de dados

a = input().split()

#Processamento de dados

b = float(a[0])
c = float(a[1])
d = float(a[2])

Tri = (b*d)/2
Cir = pi*(d**2)
Tra = ((b+c)*d)/2
Qua = c**2
Ret = b*c

#Saída de dados

print(f'TRIANGULO: {Tri:.3f}')
print(f'CIRCULO: {Cir:.3f}')
print(f'TRAPEZIO: {Tra:.3f}')
print(f'QUADRADO: {Qua:.3f}')
print(f'RETANGULO: {Ret:.3f}')
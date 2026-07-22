# Resolução do exercicio bc 1036 - Bhaskara's Formula

# input

valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

# data processing

delta = b**2 - (4*a*c)

if delta < 0 or a == 0:
    print("Impossivel calcular")

else:
    raizDelta = delta**0.5

    raiz1 = (-b + raizDelta)/(2*a)
    raiz2 = (-b - raizDelta)/(2*a)
    
    # output
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")

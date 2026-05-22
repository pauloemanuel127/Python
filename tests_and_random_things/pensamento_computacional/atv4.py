#Atividade 4 para a disciplina de pensamento computacional

valores = input().split()
valores = [float(valores[0]), float(valores[1]), float(valores[2])]
valores.sort()

l3 = valores[0]
l2 = valores[1]
l1 = valores[2]

quadrado_l1 = round(l1 ** 2, 4)
soma_dos_quadrados = round ((l2 ** 2) + (l3 ** 2), 4)

if l1 >= (l2 + l3):
    print("NAO FORMA TRIANGULO")

elif quadrado_l1 == soma_dos_quadrados:
    print("TRIANGULO RETANGULO")
    
    if l1 == l3:
        print("TRIANGULO EQUILATERO")
    
    elif l2 == l3 or l1 == l2:
        print("TRIANGULO ISOSCELES")

elif quadrado_l1 > soma_dos_quadrados:
    print("TRIANGULO OBTUSANGULO")
    
    if l1 == l3:
        print("TRIANGULO EQUILATERO")
    
    elif l2 == l3 or l1 == l2:
        print("TRIANGULO ISOSCELES")

elif quadrado_l1 < soma_dos_quadrados:
    print("TRIANGULO ACUTANGULO")

    if l1 == l3:
        print("TRIANGULO EQUILATERO")
    
    elif l2 == l3 or l1 == l2:
        print("TRIANGULO ISOSCELES")
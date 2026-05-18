#Resolução do exercicio BC 1035 - Selection Test 1

#This exercise requires a long condicional if, who test all the wanted cases for the program input validate
#If validate True print "Valores aceitos", If not validate print "Valores nao aceitos"

valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2) == 0:

    print("Valores aceitos")

else:

    print("Valores nao aceitos") 
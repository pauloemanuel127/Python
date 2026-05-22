n1 = float(input())
n2 = float(input())
n3 = float(input())

media = float(((n1 * 2)+(n2 * 3)+(n3 * 4)) / 9)

if media < 3:
    print("Francisco está reprovado")

elif media < 7:
    print("Francisco está em prova final")

else:
    print("Francisco está aprovado")
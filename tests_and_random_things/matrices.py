matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

pares = 0
c3 = 0
maior2 = matriz [1] [0]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input())

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end= "")
    print("")
    if matriz[l][c] % 2 == 0:
        pares += matriz[l][c]
print(pares)

for l in range (0, 3):
    c3 += matriz[l][2]
print(c3)

for c in range(0, 3):
    if matriz[1][c] > maior2:
        maior2 = matriz[1][c]
print(maior2)
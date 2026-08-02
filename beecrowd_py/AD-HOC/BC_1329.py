#Resolução do exercicio BC 1329 - Head or Tail

#This program receives a integer input with the number of coins flipped,
#After this, the program expects a input with the results in one line,
#checks who win and registers it. When the case ends, it prints the result.
#The program breaks after the number of coins flipped equals 0.

while True:

    jogadas = int(input())
    mary = 0
    john = 0

    if jogadas == 0:

        break

    resultados = input().split()

    for i in range(0, jogadas):

        caso = int(resultados[i])

        if caso == 0:
            mary += 1
        elif caso == 1:
            john += 1

    print(f"Mary won {mary} times and John won {john} times")
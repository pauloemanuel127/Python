#Atividade 7 para a disciplina de pensamento computacional

testes = int(input())

for i in range (0, testes):

    torre = input().split()
    X = int(torre[0]) - 1
    Y = int(torre[1])
    soma = 0
    total = 0

    while soma < Y:

        X += 1

        if X % 2 != 0:
            
            total += X
            soma +=1
      
    print(total)
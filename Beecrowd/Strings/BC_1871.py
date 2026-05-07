#Resolução do exercicio BC 1871 - Zero means Zero

#Input
while True:
    valores = input().split()

    A = int(valores[0])
    B = int(valores[1])

    #Data processing

    if A != 0 and B !=0:

        C = A+B
        C = str(C)
        C = str.replace(C, "0", "")

        #Output
        print(C)

    else:
        
        break
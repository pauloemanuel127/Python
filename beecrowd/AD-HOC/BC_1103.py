#Resolução do exercicio BC 1103 - Alarm Clock

#input

while True:
    try:
        horario = input().split()
        inicio = horario[0], horario[1]
        final = horario[2], horario[3]
        h0 = int(horario[0])
        h1 = int(horario[1])
        h2 = int(horario[2])
        h3 = int(horario[3])

        #Data processing

        if inicio == ('0', '0') and final == ('0', '0'):
            break
        elif h2 > h0 or (h2 == h0 and h3 >= h1):
            minutos = ((h2 - h0) * 60) + (h3 - h1)
        else:
            minutos = 1440 + (((h2 - h0) * 60) + (h3 - h1))
        
        #output
        print(minutos)

    #EOF ending the code
    except EOFError:
        break
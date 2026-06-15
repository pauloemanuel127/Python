#Atividade 14 para a disciplina de pensamento computacional

def fuso(h0, t, f):

    hora_de_chegada = h0 + t + f

    if hora_de_chegada < 0:

        hora_de_chegada += 24
    
    elif hora_de_chegada >= 24:

        hora_de_chegada = hora_de_chegada - 24        

    print(f"Hora de saída: {h0}")
    print(f"Hora de chegada: {hora_de_chegada}")

hora_de_saida = int(input())
duração = int(input())
diff = int(input())

fuso(hora_de_saida, duração, diff)
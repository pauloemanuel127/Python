#Atividade 1 para a disciplina de pensamento computacional

valor =  int(input())
forma = input()

if forma == "V":

    valor = int(valor - ((valor * 5) / 100))

    print(f"Valor a pagar: {valor}")

elif forma == "P":

    taxa = int((valor * 8) / 100)
    parcela = int((valor + taxa) / 3)

    print(f"Valor a pagar: {valor + taxa}")

    for i in range(1, 4):
        print(f"Parcela {i}: {parcela}")
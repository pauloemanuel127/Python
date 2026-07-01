#Atividade 11 para a disciplina de pensamento computacional

entrada = input().strip("[]")
entrada = entrada.replace(", ", ",")
entrada = entrada.split(",")
valor = input()
substituto = input()

if valor in entrada:

    for i in range(len(entrada)):

        if entrada[i] == valor:
            entrada[i] = substituto
            
    print(entrada)


else:
    print("Item não presente no inventário.")

#Atividade 9 para a disciplina de pensamento computacional

def validate(notas):

    if len(notas) < 2:
        print("Não é possível determinar o segundo maior valor com menos de dois elementos.")
        return False
    
    else:
        valor = float(notas[0])
        for i in range(1, len(notas)):

            if valor != float(notas[i]):
                return True
        print("Não é possível determinar o segundo maior valor com menos de dois valores distintos.")
        return False
            
notas = input().split(", ")

if validate(notas) is True:

    if float(notas[0]) > float(notas[1]):
        maior = float(notas[0])
        segundo_maior = float(notas[1])

    else:
        maior = float(notas[1])
        segundo_maior = float(notas[0])

    for i in range(2, len(notas)):

        if maior < float(notas[i]):
            segundo_maior = maior
            maior = float(notas[i])

        elif float(notas[i]) > segundo_maior and float(notas[i]) != maior:
            segundo_maior = float(notas[i])
   
    print(segundo_maior)     
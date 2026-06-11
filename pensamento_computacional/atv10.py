#Atividade 10 para a disciplina de pensamento computacional

def achatar_lista(lista):

    lista_final = []
    
    for item in lista:

        if isinstance(item, list):
            lista_final.extend(achatar_lista(item))
        
        else:
            lista_final.append(item)

    return lista_final

lista = input()
lista = eval(lista)
resultado = achatar_lista(lista)

print(resultado)
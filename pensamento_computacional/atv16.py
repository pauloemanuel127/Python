#Atividade 16 para a disciplina de pensamento computacional

def validar(email):
    """
    Recebe uma string que deverá ser um email, 
    a separa usando os indices, 
    e retorna apenas o dominio do email
    """
    pos_arroba = email.find("@")
    pos_ponto = email.find(".", pos_arroba)

    return email[pos_arroba + 1 : pos_ponto]

while True:

    email = input()

    if email == "FIM":
        break

    else:
        endereço = validar(email)
        print(endereço)
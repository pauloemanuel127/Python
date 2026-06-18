#Atividade 15 para a disciplina de pensamento computacional

def get_range(n, cells, distance, user):
    """
    Recebe o numero de antenas, a lista de posição das antenas, a distancia maxima que elas operam, e a posição do usuario.
    Com isso calcula se ele está no alcance de alguma antena e caso esteja adiciona a antena a uma lista de conexões, 
    se não estiver retorna uma lista vazia.
    """

    def conexion_check(pos_celula, distancia, pos_user):
        """
        Verifica se o usuario está conectado na antena escolhida
        """

        if pos_user > pos_celula:
            if distancia >= (pos_user - pos_celula):
                return True
            
        else:
            if distancia >= (pos_celula - pos_user):
                return True
            
        return False

    conexões = []

    for j in range(0, n):
        result = conexion_check(cells[j], distance, user)
        
        if result is True:
            conexões.append(cells[j])

    return conexões
    

valores = input().split()

n = int(valores[0])
cells = []
distance = int(valores[1])
user = int(valores[2])

for i in range(n):
    cell = int(input())
    cells.append(cell)

resultado = get_range(n, cells, distance, user)

if len(resultado) == 0:
    print("USUARIO DESCONECTADO")

else:
    print(*(resultado))
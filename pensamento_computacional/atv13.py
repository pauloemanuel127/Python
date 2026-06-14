#Atividade 13 para a disciplina de pensamento computacional

def gemeos(n):
    """
    Verifica se o valor digitado na entrada é primo gêmeo
    """

    if n <= 1:
        return False
    
    else:

        gemeo = n+2

        for i in range(n+1, 1, -1):

            if i != n and n % i == 0:
                return False
            
            if (gemeo % i) == 0:
                return False
            
        return True
        
test = int(input())

if gemeos(test) == True:
    print("Número forma par de gêmeos")

else:
    print("Número não forma par de gêmeos")
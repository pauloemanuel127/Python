#Resolução do exercico BC 1129 - optical reader

while True:

    n_questoes = int(input())

    if n_questoes != 0:

        for i in range(n_questoes):

            valores = input().split()
            A = int(valores[0])
            B = int(valores[1])
            C = int(valores[2])
            D = int(valores[3])
            E = int(valores[4])
            
            if A <= 127 and B > 127 and C > 127 and D > 127 and E > 127:
                print('A')
            elif A > 127 and B <= 127 and C > 127 and D > 127 and E > 127:
                print('B')
            elif A > 127 and B > 127 and C <= 127 and D > 127 and E > 127:
                print('C')
            elif A > 127 and B > 127 and C > 127 and D <= 127 and E > 127:
                print('D')
            elif A > 127 and B > 127 and C > 127 and D > 127 and E <= 127:
                print('E')        
            else:
                print('*')

    else:
        break
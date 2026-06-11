#Atividade 12 para a disciplina de pensamento computacional

n_testes = int(input())

for i in range(n_testes):

    lista = []
    lista_nova = []
    mudanças = 0

    alunos = int(input())
    notas = input().split()
    for j in range(alunos):

        lista.append(int(notas[j]))
        lista_nova.append(int(notas[j]))
  
    lista_nova.sort(reverse=True)

    for k in range(len(lista)):

        if lista[k] == lista_nova[k]:
            mudanças += 1
    
    print(mudanças)
#Atividade 8 para a disciplina de pensamento computacional

testes = int(input())

for i in range(0, testes):

    valores = input().split()
    pa = int(valores[0])
    pb = int(valores[1])
    g1 = float(valores[2])
    g2 = float(valores[3])
    anos = 0
   
    while pa <= pb:
        
        pa = pa + ((pa*g1)//100) 
        pb = pb + ((pb*g2)//100)
        anos = anos + 1

    if anos > 100:
        print("Mais de 1 seculo.")
    
    else:
        print(f"{anos} anos.")
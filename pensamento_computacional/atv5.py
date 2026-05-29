#Atividade 5 para a disciplina de pensamento computacional

dna = int(input())
fatorial = 1

if dna != 0:
    for i in range(1, (dna + 1)):
        fatorial = fatorial * i 
    print(f"Resultado do fatorial: {fatorial}")

else:
    print("O número deve ser maior que 0.")
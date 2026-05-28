#Atividade 6 para a disciplina de pensamento computacional

valor = float(input())
maior = valor

if valor != 0:

    while valor != 0:

        valor = float(input())

        if valor > maior:
            maior = valor

    print(f"O seu maior gasto hoje foi R$ {maior:.2f}")

else:
    print("Você não teve gastos hoje!")   
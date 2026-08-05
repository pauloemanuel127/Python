#Resolução do exercicio BC 1042 - Average 3

notas = input().split()

N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])

media = ((N1 * 2.0) + (N2 * 3.0) + (N3 * 4.0) + N4)/10

print(f"Media: {media:.1f}")

if media >= 7.0:

    print("Aluno aprovado.")

elif 5.0 <= media <= 6.9:

    print("Aluno em exame.")

    exame = float(input())

    nota_final = (media + exame) / 2

    print(f"Nota do exame: {exame:.1f}")

    if nota_final >= 5.0:

        print("Aluno aprovado.")

    else:

        print("Aluno reprovado.")

    print(f"Media final: {nota_final:.1f}")

else:

    print("Aluno reprovado.")
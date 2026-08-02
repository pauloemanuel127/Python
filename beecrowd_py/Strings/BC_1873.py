#Resolução do exercicio BC 1873 - Rock-paper-scissors-lizard-Spock

#This program works like a rock, paper, scissors game with two additional values.
#I choose the first player to be the anchor and make the results with his possibilities

partidas = int(input())

for i in range(partidas):
    jogadas = input().split()
    raj = jogadas[0]
    sheldon = jogadas[1]
    if raj == sheldon:
        print("empate")
    elif raj == "tesoura" and (sheldon == "papel" or sheldon == "lagarto"):
            print("rajesh")
    elif raj == "papel" and (sheldon == "pedra" or sheldon == "spock"):
            print("rajesh")
    elif raj == "pedra" and (sheldon == "tesoura" or sheldon == "lagarto"):
            print("rajesh")
    elif raj == "lagarto" and (sheldon == "papel" or sheldon == "spock"):
            print("rajesh")
    elif raj == "spock" and (sheldon == "pedra" or sheldon == "tesoura"):
            print("rajesh")
    else:
        print("sheldon")
# Resolução do exercicio bc 1037 - Interval

# input

entrada = float(input())

# data processing

if entrada >= 0:

    # outputs

    if entrada <= 25.0000:
        print("Intervalo [0,25]")

    elif entrada <= 50.0000:
        print("Intervalo (25,50]")

    elif entrada <= 75.0000:
        print("Intervalo (50,75]")

    elif entrada <= 100.0000:
        print("Intervalo (75,100]")
    
    else:
        print("Fora de intervalo")

else:
    print("Fora de intervalo")
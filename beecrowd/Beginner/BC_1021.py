#Resolução do exercicio BC 1021 - notes and coins

#Data input and variables
#Here the variables is defined to become usable in the loop

valor = float(input())
centavos = int(round(valor*100))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0 
nota5 = 0
nota2 = 0
moeda1 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda05 = 0
moeda01 = 0

#Data Processing,
#Here the while loops its used to make possible test how many notes and coins is necessary
#The condicinal chain test the values

while centavos > 0:
    
    if centavos >= 10000:

        centavos -= 10000
        nota100 += 1

    elif centavos >= 5000:

        centavos -= 5000
        nota50 += 1

    elif centavos >= 2000:

        centavos -= 2000
        nota20 += 1

    elif centavos >= 1000:

        centavos -= 1000
        nota10 += 1

    elif centavos >= 500:

        centavos -= 500
        nota5 += 1

    elif centavos >= 200:

        centavos -= 200
        nota2 += 1

    elif centavos >= 100:

        centavos -= 100
        moeda1 += 1

    elif centavos >= 50:

        centavos -= 50
        moeda50 += 1

    elif centavos >= 25:

        centavos -= 25
        moeda25 += 1
    
    elif centavos >= 10:

        centavos -= 10
        moeda10 += 1
    
    elif centavos >= 5:

        centavos -= 5
        moeda05 += 1
    
    elif centavos >= 1:

        centavos -= 1
        moeda01 += 1

#Data Output

print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00") 
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda50} moeda(s) de R$ 0.50")  
print(f"{moeda25} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda05} moeda(s) de R$ 0.05")
print(f"{moeda01} moeda(s) de R$ 0.01")    
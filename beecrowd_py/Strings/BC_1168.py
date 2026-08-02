#Resolução do Exercicio BC 1168 - LED

#The first input recevies the number of test cases,
#This integer is used in the for loop to defines the number of repetitions
#Inside the loop, its recived a string,
#Who represents the number wanted do be maked with the leds
#In the second loop we use pick each char in the input
#And test in the condicional chain
#In the end the outputs send the number of leds 

casos_teste = int(input())

for i in range(casos_teste):
    numero = input()
    leds = 0
    for char in numero:
        if char == "1":
            leds += 2
        elif char == "2" or char == "3" or char == "5":
            leds += 5
        elif char == "4":
            leds += 4
        elif char == "6" or char == "9" or char == "0":
            leds += 6
        elif char == "7":
            leds += 3
        elif char == "8":
            leds += 7
    print(f"{leds} leds")



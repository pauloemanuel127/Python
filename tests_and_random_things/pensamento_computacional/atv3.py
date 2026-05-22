#Atividade 3 para a disciplina de pensamento computacional

temperatura = input().split()

if temperatura[1] == "C":
    valor = float(temperatura[0])
    fahrenheit = (valor * 1.8) + 32
    kelvin = valor + 273.15
    print(f"Temperatura em Celsius: {valor:.2f} °C")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura em Kelvin: {kelvin:.2f} K")

elif temperatura[1] == "F":
    valor = float(temperatura[0])
    celsius = (valor - 32) / 1.8
    kelvin = ((valor - 32) / 1.8) + 273.15
    print(f"Temperatura em Celsius: {celsius:.2f} °C")
    print(f"Temperatura em Fahrenheit: {valor:.2f} °F")
    print(f"Temperatura em Kelvin: {kelvin:.2f} K")

elif temperatura[1] == "K":
    valor = float(temperatura[0])
    celsius = valor - 273.15
    fahrenheit = ((valor - 273.15) * 1.8) + 32 
    print(f"Temperatura em Celsius: {celsius:.2f} °C")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura em Kelvin: {valor:.2f} K")
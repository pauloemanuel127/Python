#Resolução do exercicio BC 1038 - Snack

entrada = input().split()
quant = int(entrada[1])
total = 0

if entrada[0] == '1':
    
    total = quant * 4.00
    
elif entrada [0] == '2':
    
    total = quant * 4.50

elif entrada[0] == '3':
    
    total = quant * 5.00
    
elif entrada[0] == '4':
    
    total = quant * 2.00
    
elif entrada[0] == '5':
    
    total = quant * 1.50
    
print(f"Total: R$ {total:.2f}")
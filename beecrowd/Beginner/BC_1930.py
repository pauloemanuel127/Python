#Resolução do exercicio BC 1930 - Eletrical Outlet

#Input

power_strips = input().split()
t1 = int(power_strips[0])
t2 = int(power_strips[1])
t3 = int(power_strips[2])
t4 = int(power_strips[3])

#Data processing

total = (t1 + t2 + t3 + t4) - 3

#Output

print(total)
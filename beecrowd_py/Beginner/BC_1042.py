#Resolução do exercicio BC 1042 - simple sort

#input

input = input().split()
values = [int(input[0]), int(input[1]), int(input[2])]

#data processing

#the line n = len(values) count how many elements are in the list/array
n = len(values)
#this for line starts and define that the list its already sorted, 
#then in the second for loop test if its true,
#if it is necessary to replace one element with other,
#he defines that the list isn't sorted and loops again, until the list is sorted.
#if the list literally already sorted,
#In the second loop, it will go straight through and the program will end sooner.
for i in range(n-1):
    already_sorted = True
    for j in range(n - i - 1):
        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]
            already_sorted = False
    if already_sorted:
        break
        

#output
print(values[0])
print(values[1])
print(f"{values[2]}\n")
print(input[0])
print(input[1])
print(input[2])

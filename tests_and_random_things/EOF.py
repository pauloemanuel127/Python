#How to EOF

#The while True loop function stop working when the computer run out of memory, 
#because the program enter the except block due to the EOFError.
while True:
    try:
        entrada = input().split()
        a = int(entrada[0])
        b = int(entrada[1])

        print(f"{a} e {b}")

    except EOFError:
        break
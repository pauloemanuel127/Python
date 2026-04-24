#How to EOF

#The while True loop function stop when the program runs out of input and enter the EOFError, 
#because the program enter the except block due to the EOFError.
while True:
    try:
        entrada = input().split()
        a = int(entrada[0])
        b = int(entrada[1])

        print(f"{a} e {b}")

    except EOFError:
        break
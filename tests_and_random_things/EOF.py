#How to EOF

#The while True loop function stops whens there is no more input data do be read, 
#triggering the EOFError and breaking the loop.
while True:
    try:
        entrada = input().split()
        a = int(entrada[0])
        b = int(entrada[1])

        print(f"{a} e {b}")

    except EOFError:
        break
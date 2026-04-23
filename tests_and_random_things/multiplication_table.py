#This code its a multiplication table calculator

#The while True heres makes the code work until the EOF
while True:

    #This try tests if the computer have memory, if not occurs the EOFerror
    try:
        #Input 
        #(The input here recevies the number whose multiplication table the user wants to know.)
        X = input('Caso deseje sair da aplicação digite "exit"\nDigite o número que você deseja saber a tabuada:\n')
        #Data processing 
        #(The if conditional tests if the user wants to exit)
        #(in the else block, the code try if the value on input its a number,
        #if its True, the code continue, and print the multiplication table)
        if X == 'exit':
            break
        else:
            try:
                X = float(X)
                for i in range(1, 11):
                    print(f'{X} x {i} = {X*i:.2f}')
                print('')
            except ValueError:
                print('Digite um numero ou "exit"\n')
    except EOFError:
        break
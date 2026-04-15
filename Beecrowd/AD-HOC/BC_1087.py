#Resolução do exercicio BC 1087 - Queen

#input
while True:
    moves = input().split()
    x1 = int(moves[0])
    y1 = int(moves[1])
    x2 = int(moves[2])
    y2 = int(moves[3])
    X = (x1, y1)
    Y = (x2, y2)
    #In this part of the code, the `if` statement checks if the input is true with respect to the chessboard,
    #or, if the input is responsible for the interruption condition; otherwise, it defines that the input is not true with respect to the chessboard.
    #Then, another `if` statement checks how many moves the queen will make.
    if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
        if X == Y:
            print('0')
        elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            print('1')
        else:
            print('2')
    elif x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        break
    else:
        print('The input values do not correspond to the format of a chessboard')
        
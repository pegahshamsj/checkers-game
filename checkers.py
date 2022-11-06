import random
import sys

# first initialization
board = [["__" for x in range(9)] for y in range(9)]

w0 = 100
w1 = -1
w2 = 1
w3 = -1
w4 = 1
w5 = 1
w6 = -1

numberOfBlack = 12
numberOfWhite = 12
numberOfKingBlack = 0
numberOfKingWhite = 0
numberOfInDangerBlack = 0
numberOfInDangerWhite = 0

fi = 100
error = 0
w_finish = 0
b_finish = 0
result = 2
finish = True
n = 0
results = []


# evaluation function
def value(number_of_black, number_of_white, number_of_king_black, number_of_king_white, number_of_in_danger_black,
          number_of_in_danger_white, w_0, w_1, w_2, w_3, w_4, w_5, w_6):
    return w_0 + (w_1 * number_of_black) + (w_2 * number_of_white) + (w_3 * number_of_king_black) + \
           (w_4 * number_of_king_white) + (w_5 * number_of_in_danger_black) + (w_6 * number_of_in_danger_white)


# finding number of white in danger
def white_in_danger_recognition(wid):
    number_of_in_danger_white = 0

    for b in range(1, 9):
        for a in range(1, 9):

            if wid[a][b] == "-1" and 1 <= a + 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (wid[a + 1][b + 1] == " 1" or wid[a + 1][b + 1] == " 2") and wid[a + 2][b + 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

            if wid[a][b] == "-1" and 1 <= a + 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (wid[a + 1][b - 1] == " 1" or wid[a + 1][b - 1] == " 2") and wid[a + 2][b - 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

            if wid[a][b] == "-2" and 1 <= a + 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (wid[a + 1][b + 1] == " 1" or wid[a + 1][b + 1] == " 2") and wid[a + 2][b + 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

            if wid[a][b] == "-2" and 1 <= a - 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (wid[a - 1][b - 1] == " 1" or wid[a - 1][b - 1] == " 2") and wid[a - 2][b - 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

            if wid[a][b] == "-2" and 1 <= a - 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (wid[a - 1][b + 1] == " 1" or wid[a - 1][b + 1] == " 2") and wid[a - 2][b + 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

            if wid[a][b] == "-2" and 1 <= a + 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (wid[a + 1][b - 1] == " 1" or wid[a + 1][b - 1] == " 2") and wid[a + 2][b - 2] == "__":
                number_of_in_danger_white = number_of_in_danger_white + 1

    return number_of_in_danger_white


# finding number of black in danger
def black_in_danger_recognition(bid):
    number_of_in_danger_black = 0

    for b in range(1, 9):
        for a in range(1, 9):

            if bid[a][b] == " 1" and 1 <= a - 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (bid[a - 1][b - 1] == "-1" or bid[a - 1][b - 1] == "-2") and bid[a - 2][b - 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

            if bid[a][b] == " 1" and 1 <= a - 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (bid[a - 1][b + 1] == "-1" or bid[a - 1][b + 1] == "-2") and bid[a - 2][b + 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

            if bid[a][b] == " 2" and 1 <= a + 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (bid[a + 1][b + 1] == "-1" or bid[a + 1][b + 1] == "-2") and bid[a + 2][b + 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

            if bid[a][b] == " 2" and 1 <= a - 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (bid[a - 1][b - 1] == "-1" or bid[a - 1][b - 1] == "-2") and bid[a - 2][b - 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

            if bid[a][b] == " 2" and 1 <= a - 2 <= 8 and 1 <= b + 2 <= 8 and \
                    (bid[a - 1][b + 1] == "-1" or bid[a - 1][b + 1] == "-2") and bid[a - 2][b + 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

            if bid[a][b] == " 2" and 1 <= a + 2 <= 8 and 1 <= b - 2 <= 8 and \
                    (bid[a + 1][b - 1] == "-1" or bid[a + 1][b - 1] == "-2") and bid[a + 2][b - 2] == "__":
                number_of_in_danger_black = number_of_in_danger_black + 1

    return number_of_in_danger_black


# condition for continuing the game
while n != 500:

    print(n)
    n = n + 1

    board = [["__" for x in range(9)] for y in range(9)]

    # horizontal indices
    for j in range(9):
        for i in range(1):
            board[i][j] = " " + str(j)

    # vertical indices
    for j in range(1):
        for i in range(9):
            board[i][j] = str(i)

    # black line 0 and 3
    for j in range(2, 9, 2):
        for i in range(1, 4, 2):
            board[i][j] = "-1"

    # black line 2
    for j in range(1, 9, 2):
        for i in range(2, 3):
            board[i][j] = "-1"

    # white line 0 and 3
    for j in range(1, 9, 2):
        for i in range(6, 9, 2):
            board[i][j] = " 1"

    # white line 2
    for j in range(2, 9, 2):
        for i in range(7, 8):
            board[i][j] = " 1"

    numberOfBlack = 12
    numberOfWhite = 12
    numberOfKingBlack = 0
    numberOfKingWhite = 0
    numberOfInDangerBlack = 0
    numberOfInDangerWhite = 0
    w_finish = 0
    b_finish = 0
    result = 2
    finish = True
    error = 0
    m = 0
    fi = w0

    while finish and m != 200:

        m = m + 1

        # white move
        w_values = {}
        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 1white move 1 step
                if board[i][j] == " 1" and result == 2:

                    # right direction 1 step
                    if 1 <= i - 1 <= 8 and 1 <= j + 1 <= 8 and board[i - 1][j + 1] == "__":
                        w_values[i, j, "R", 1] = 1

                    # left direction 1 step
                    if 1 <= i - 1 <= 8 and 1 <= j - 1 <= 8 and board[i - 1][j - 1] == "__":
                        w_values[i, j, "L", 2] = 2

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 1white move 2 step
                if board[i][j] == " 1" and result == 2:

                    # right direction 2 steps
                    if 1 <= i - 2 <= 8 and 1 <= j + 2 <= 8 and board[i - 2][j + 2] == "__" and \
                            (board[i - 1][j + 1] == "-1" or board[i - 1][j + 1] == "-2"):
                        w_values[i, j, "R", 3] = 3

                    # left direction 2 steps
                    if 1 <= i - 2 <= 8 and 1 <= j - 2 <= 8 and board[i - 2][j - 2] == "__" and \
                            (board[i - 1][j - 1] == "-1" or board[i - 1][j - 1] == "-2"):
                        w_values[i, j, "L", 4] = 4

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 2white move 1 step up
                if board[i][j] == " 2" and result == 2:

                    # right direction 1 step
                    if 1 <= i - 1 <= 8 and 1 <= j + 1 <= 8 and board[i - 1][j + 1] == "__":
                        w_values[i, j, "R", 5] = 5

                    # left direction 1 step
                    if 1 <= i - 1 <= 8 and 1 <= j - 1 <= 8 and board[i - 1][j - 1] == "__":
                        w_values[i, j, "L", 6] = 6

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 2white move 2 step up
                if board[i][j] == " 2" and result == 2:

                    # right direction 1 step
                    if 1 <= i - 2 <= 8 and 1 <= j + 2 <= 8 and board[i - 2][j + 2] == "__" and \
                            (board[i - 1][j + 1] == "-1" or board[i - 1][j + 1] == "-2"):
                        w_values[i, j, "R", 7] = 7

                    # left direction 1 step
                    if 1 <= i - 2 <= 8 and 1 <= j - 2 <= 8 and board[i - 2][j - 2] == "__" and \
                            (board[i - 1][j - 1] == "-1" or board[i - 1][j - 1] == "-2"):
                        w_values[i, j, "L", 8] = 8

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 2white move 1 step down
                if board[i][j] == " 2" and result == 2:

                    # right direction 1 step
                    if 1 <= i + 1 <= 8 and 1 <= j + 1 <= 8 and board[i + 1][j + 1] == "__":
                        w_values[i, j, "R", 9] = 9

                    # left direction 1 step
                    if 1 <= i + 1 <= 8 and 1 <= j - 1 <= 8 and board[i + 1][j - 1] == "__":
                        w_values[i, j, "L", 10] = 10

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper 2white move 2 step down
                if board[i][j] == " 2" and result == 2:

                    # right direction 1 step
                    if 1 <= i + 2 <= 8 and 1 <= j + 2 <= 8 and board[i + 2][j + 2] == "__" and \
                            (board[i + 1][j + 1] == "-1" or board[i + 1][j + 1] == "-2"):
                        w_values[i, j, "R", 11] = 11

                    # left direction 1 step
                    if 1 <= i + 2 <= 8 and 1 <= j - 2 <= 8 and board[i + 2][j - 2] == "__" and \
                            (board[i + 1][j - 1] == "-1" or board[i + 1][j - 1] == "-2"):
                        w_values[i, j, "L", 12] = 12

        if bool(w_values) == False:
            w_finish = 1
            if (numberOfBlack != 0 or numberOfKingBlack != 0) and (numberOfWhite == 0 and numberOfKingWhite == 0):
                finish = False
                result = -1
                break
            elif w_finish == 1 and b_finish == 1:
                finish = False
                result = 0
                break
            elif b_finish == 0 and w_finish == 1:
                finish = False
                result = -1
                break

        # print the move on the board
        else:
            w_move = random.choice(list(w_values.keys()))
            # print(w_move)
            if w_move[3] == 1:
                if w_move[0] - 1 == 1 and board[w_move[0]][w_move[1]] == " 1":
                    board[w_move[0] - 1][w_move[1] + 1] = " 2"
                    numberOfWhite = numberOfWhite - 1
                    numberOfKingWhite = numberOfKingWhite + 1
                else:
                    board[w_move[0] - 1][w_move[1] + 1] = " 1"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 2:
                if w_move[0] - 1 == 1 and board[w_move[0]][w_move[1]] == " 1":
                    board[w_move[0] - 1][w_move[1] - 1] = " 2"
                    numberOfWhite = numberOfWhite - 1
                    numberOfKingWhite = numberOfKingWhite + 1
                else:
                    board[w_move[0] - 1][w_move[1] - 1] = " 1"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 3:
                if w_move[0] - 2 == 1 and board[w_move[0]][w_move[1]] == " 1":
                    board[w_move[0] - 2][w_move[1] + 2] = " 2"
                    if board[w_move[0] - 1][w_move[1] + 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] + 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] + 1] = "__"
                    numberOfWhite = numberOfWhite - 1
                    numberOfKingWhite = numberOfKingWhite + 1
                else:
                    board[w_move[0] - 2][w_move[1] + 2] = " 1"
                    if board[w_move[0] - 1][w_move[1] + 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] + 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] + 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 4:
                if w_move[0] - 2 == 1 and board[w_move[0]][w_move[1]] == " 1":
                    board[w_move[0] - 2][w_move[1] - 2] = " 2"
                    if board[w_move[0] - 1][w_move[1] - 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] - 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] - 1] = "__"
                    numberOfWhite = numberOfWhite - 1
                    numberOfKingWhite = numberOfKingWhite + 1
                else:
                    board[w_move[0] - 2][w_move[1] - 2] = " 1"
                    if board[w_move[0] - 1][w_move[1] - 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] - 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] - 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 5:
                board[w_move[0] - 1][w_move[1] + 1] = " 2"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 6:
                board[w_move[0] - 1][w_move[1] - 1] = " 2"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 7:
                if board[w_move[0]][w_move[1]] == " 2":
                    board[w_move[0] - 2][w_move[1] + 2] = " 2"
                    if board[w_move[0] - 1][w_move[1] + 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] + 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] + 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 8:
                if board[w_move[0]][w_move[1]] == " 2":
                    board[w_move[0] - 2][w_move[1] - 2] = " 2"
                    if board[w_move[0] - 1][w_move[1] - 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] - 1][w_move[1] - 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] - 1][w_move[1] - 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 9:
                board[w_move[0] + 1][w_move[1] + 1] = " 2"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 10:
                board[w_move[0] + 1][w_move[1] - 1] = " 2"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 11:
                if board[w_move[0]][w_move[1]] == " 2":
                    board[w_move[0] + 2][w_move[1] + 2] = " 2"
                    if board[w_move[0] + 1][w_move[1] + 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] + 1][w_move[1] + 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] + 1][w_move[1] + 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

            elif w_move[3] == 12:
                if board[w_move[0]][w_move[1]] == " 2":
                    board[w_move[0] + 2][w_move[1] - 2] = " 2"
                    if board[w_move[0] + 1][w_move[1] - 1] == "-1":
                        numberOfBlack = numberOfBlack - 1
                    elif board[w_move[0] + 1][w_move[1] - 1] == "-2":
                        numberOfKingBlack = numberOfKingBlack - 1
                    board[w_move[0] + 1][w_move[1] - 1] = "__"
                board[w_move[0]][w_move[1]] = "__"

        # black move
        values = {}
        di = 0
        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -1black move 1 step
                if board[i][j] == "-1" and result == 2:

                    # right direction 1 step
                    if (i + 1) <= 8 and (j + 1) <= 8 and board[i + 1][j + 1] == "__":
                        board[i][j] = "__"
                        board[i + 1][j + 1] = "-1"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        e = 0
                        if i + 1 == 8:
                            numberOfKingBlack = numberOfKingBlack + 1
                            numberOfBlack = numberOfBlack - 1
                            e = 3
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if e == 3:
                            numberOfKingBlack = numberOfKingBlack - 1
                            numberOfBlack = numberOfBlack + 1
                            e = 0
                        board[i][j] = "-1"
                        board[i + 1][j + 1] = "__"
                        di = 1
                        values[i, j, "R", di] = point

                    # left direction 1 step
                    if (i + 1) <= 8 and (j - 1) >= 0 and board[i + 1][j - 1] == "__":
                        board[i][j] = "__"
                        board[i + 1][j - 1] = "-1"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        e = 0
                        if i + 1 == 8:
                            numberOfKingBlack = numberOfKingBlack + 1
                            numberOfBlack = numberOfBlack - 1
                            e = 3
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if e == 3:
                            numberOfKingBlack = numberOfKingBlack - 1
                            numberOfBlack = numberOfBlack + 1
                            e = 0
                        board[i][j] = "-1"
                        board[i + 1][j - 1] = "__"
                        di = 2
                        values[i, j, "L", di] = point

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -1black move 2 step
                if board[i][j] == "-1" and result == 2:

                    # right direction 2 steps
                    if (i + 2) <= 8 and (j + 2) <= 8 and board[i + 2][j + 2] == "__" and (board[i + 1][j + 1] == " 1" or
                                                                                          board[i + 1][j + 1] == " 2"):
                        board[i][j] = "__"
                        board[i + 2][j + 2] = "-1"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        e = 0
                        if board[i + 1][j + 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i + 1][j + 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        if i + 2 == 8:
                            numberOfKingBlack = numberOfKingBlack + 1
                            numberOfBlack = numberOfBlack - 1
                            e = 3
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        if e == 3:
                            numberOfKingBlack = numberOfKingBlack - 1
                            numberOfBlack = numberOfBlack + 1
                            e = 0
                        board[i][j] = "-1"
                        board[i + 2][j + 2] = "__"
                        di = 3
                        values[i, j, "R", di] = point

                    # left direction 2 steps
                    if (i + 2) <= 8 and (j - 2) >= 0 and board[i + 2][j - 2] == "__" and (board[i + 1][j - 1] == " 1" or
                                                                                          board[i + 1][j - 1] == " 2"):
                        board[i][j] = "__"
                        board[i + 2][j - 2] = "-1"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        e = 0
                        if board[i + 1][j - 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i + 1][j - 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        if i + 2 == 8:
                            numberOfKingBlack = numberOfKingBlack + 1
                            numberOfBlack = numberOfBlack - 1
                            e = 3
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        if e == 3:
                            numberOfKingBlack = numberOfKingBlack - 1
                            numberOfBlack = numberOfBlack + 1
                            e = 0
                        board[i][j] = "-1"
                        board[i + 2][j - 2] = "__"
                        di = 4
                        values[i, j, "L", di] = point

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -2black move 1 step up
                if board[i][j] == "-2" and result == 2:

                    # right direction 1 step
                    if (i - 1) >= 0 and (j + 1) <= 8 and board[i - 1][j + 1] == "__":
                        board[i][j] = "__"
                        board[i - 1][j + 1] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        board[i][j] = "-2"
                        board[i - 1][j + 1] = "__"
                        di = 5
                        values[i, j, "R", di] = point

                    # left direction 1 step
                    if (i - 1) >= 0 and (j - 1) >= 0 and board[i - 1][j - 1] == "__":
                        board[i][j] = "__"
                        board[i - 1][j - 1] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        board[i][j] = "-2"
                        board[i - 1][j - 1] = "__"
                        di = 6
                        values[i, j, "L", di] = point

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -2black move 2 step up
                if board[i][j] == "-2" and result == 2:

                    # right direction 1 step
                    if (i - 2) >= 0 and (j + 2) <= 8 and board[i - 2][j + 2] == "__" and (board[i - 1][j + 1] == " 1" or
                                                                                          board[i - 1][j + 1] == " 2"):
                        board[i][j] = "__"
                        board[i - 2][j + 2] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        if board[i - 1][j + 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i - 1][j + 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        board[i][j] = "-2"
                        board[i - 2][j + 2] = "__"
                        di = 7
                        values[i, j, "R", di] = point

                    # left direction 1 step
                    if (i - 2) >= 0 and (j - 2) >= 0 and board[i - 2][j - 2] == "__" and (board[i - 1][j - 1] == " 1" or
                                                                                          board[i - 1][j - 1] == " 2"):
                        board[i][j] = "__"
                        board[i - 2][j - 2] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        if board[i - 1][j - 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i - 1][j - 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        board[i][j] = "-2"
                        board[i - 2][j - 2] = "__"
                        di = 8
                        values[i, j, "L", di] = point

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -2black move 1 step down
                if board[i][j] == "-2" and result == 2:

                    # right direction 1 step
                    if (i + 1) <= 8 and (j + 1) <= 8 and board[i + 1][j + 1] == "__":
                        board[i][j] = "-__"
                        board[i + 1][j + 1] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        board[i][j] = "-2"
                        board[i + 1][j + 1] = "__"
                        di = 9
                        values[i, j, "R", di] = point

                    # left direction 1 step
                    if (i + 1) <= 8 and (j - 1) >= 0 and board[i + 1][j - 1] == "__":
                        board[i][j] = "__"
                        board[i + 1][j - 1] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        board[i][j] = "-2"
                        board[i + 1][j - 1] = "__"
                        di = 10
                        values[i, j, "L", di] = point

        for j in range(1, 9):
            for i in range(1, 9):

                # finding a proper -2black move 2 step down
                if board[i][j] == "-2" and result == 2:

                    # right direction 1 step
                    if (i + 2) <= 8 and (j + 2) <= 8 and board[i + 2][j + 2] == "__" and (board[i + 1][j + 1] == " 1" or
                                                                                          board[i + 1][j + 1] == " 2"):
                        board[i][j] = "__"
                        board[i + 2][j + 2] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        if board[i + 1][j + 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i + 1][j + 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        board[i][j] = "-2"
                        board[i + 2][j + 2] = "__"
                        di = 11
                        values[i, j, "R", di] = point

                    # left direction 1 step
                    if (i + 2) <= 8 and (j - 2) >= 0 and board[i + 2][j - 2] == "__" and (board[i + 1][j - 1] == " 1" or
                                                                                          board[i + 1][j - 1] == " 2"):
                        board[i][j] = "__"
                        board[i + 2][j - 2] = "-2"
                        numberOfInDangerWhite = white_in_danger_recognition(board)
                        numberOfInDangerBlack = black_in_danger_recognition(board)
                        d = 0
                        if board[i + 1][j - 1] == " 1":
                            numberOfWhite = numberOfWhite - 1
                            d = 1
                        elif board[i + 1][j - 1] == " 2":
                            numberOfKingWhite = numberOfKingWhite - 1
                            d = 2
                        point = value(numberOfBlack, numberOfWhite, numberOfKingBlack, numberOfKingWhite,
                                      numberOfInDangerBlack, numberOfInDangerWhite, w0, w1, w2, w3, w4, w5, w6)
                        if d == 1:
                            numberOfWhite = numberOfWhite + 1
                            d = 0
                        elif d == 2:
                            numberOfKingWhite = numberOfKingWhite + 1
                            d = 0
                        board[i][j] = "-2"
                        board[i + 2][j - 2] = "__"
                        di = 12
                        values[i, j, "L", di] = point
        move = ()
        if bool(values) == False:
            b_finish = 1
            if (numberOfBlack == 0 and numberOfKingBlack == 0) and (numberOfWhite != 0 or numberOfKingWhite != 0):
                finish = False
                result = 1
                break
            elif w_finish == 1 and b_finish == 1:
                finish = False
                result = 0
                break
            elif b_finish == 1 and w_finish == 0:
                finish = False
                result = 1
                break

        else:
            if w_finish == 1:
                result = -1
                finish = False
            error = values[min(values, key=values.get)] - fi
            # print("error = %f" % error)
            fi = values[min(values, key=values.get)]
            move = min(values, key=values.get)
            # print("value = %f" % fi)

            # print the move on the board
            if move[3] == 1:
                if move[0] + 1 == 8 and board[move[0]][move[1]] == "-1":
                    board[move[0] + 1][move[1] + 1] = "-2"
                    numberOfBlack = numberOfBlack - 1
                    numberOfKingBlack = numberOfKingBlack + 1
                else:
                    board[move[0] + 1][move[1] + 1] = "-1"
                board[move[0]][move[1]] = "__"

            elif move[3] == 2:
                if move[0] + 1 == 8 and board[move[0]][move[1]] == "-1":
                    board[move[0] + 1][move[1] - 1] = "-2"
                    numberOfBlack = numberOfBlack - 1
                    numberOfKingBlack = numberOfKingBlack + 1
                else:
                    board[move[0] + 1][move[1] - 1] = "-1"
                board[move[0]][move[1]] = "__"

            elif move[3] == 3:
                if move[0] + 2 == 8 and board[move[0]][move[1]] == "-1":
                    board[move[0] + 2][move[1] + 2] = "-2"
                    if board[move[0] + 1][move[1] + 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] + 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] + 1] = "__"
                    numberOfBlack = numberOfBlack - 1
                    numberOfKingBlack = numberOfKingBlack + 1
                else:
                    board[move[0] + 2][move[1] + 2] = "-1"
                    if board[move[0] + 1][move[1] + 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] + 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] + 1] = "__"
                board[move[0]][move[1]] = "__"

            elif move[3] == 4:
                if move[0] + 2 == 8 and board[move[0]][move[1]] == "-1":
                    board[move[0] + 2][move[1] - 2] = "-2"
                    if board[move[0] + 1][move[1] - 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] - 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] - 1] = "__"
                    numberOfBlack = numberOfBlack - 1
                    numberOfKingBlack = numberOfKingBlack + 1
                else:
                    board[move[0] + 2][move[1] - 2] = "-1"
                    if board[move[0] + 1][move[1] - 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] - 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] - 1] = "__"
                board[move[0]][move[1]] = "__"

            elif move[3] == 5:
                board[move[0] - 1][move[1] + 1] = "-2"
                board[move[0]][move[1]] = "__"

            elif move[3] == 6:
                board[move[0] - 1][move[1] - 1] = "-2"
                board[move[0]][move[1]] = "__"

            elif move[3] == 7:
                if board[move[0]][move[1]] == "-2":
                    board[move[0] - 2][move[1] + 2] = "-2"
                    if board[move[0] - 1][move[1] + 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] - 1][move[1] + 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] - 1][move[1] + 1] = "__"
                board[move[0]][move[1]] = "__"

            elif move[3] == 8:
                if board[move[0]][move[1]] == "-2":
                    board[move[0] - 2][move[1] - 2] = "-2"
                    if board[move[0] - 1][move[1] - 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] - 1][move[1] - 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] - 1][move[1] - 1] = "__"
                board[move[0]][move[1]] = "__"

            elif move[3] == 9:
                board[move[0] + 1][move[1] + 1] = "-2"
                board[move[0]][move[1]] = "__"

            elif move[3] == 10:
                board[move[0] + 1][move[1] - 1] = "-2"
                board[move[0]][move[1]] = "__"

            elif move[3] == 11:
                if board[move[0]][move[1]] == "-2":
                    board[move[0] + 2][move[1] + 2] = "-2"
                    if board[move[0] + 1][move[1] + 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] + 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] + 1] = "__"
                board[move[0]][move[1]] = "__"

            elif move[3] == 12:
                if board[move[0]][move[1]] == "-2":
                    board[move[0] + 2][move[1] - 2] = "-2"
                    if board[move[0] + 1][move[1] - 1] == " 1":
                        numberOfWhite = numberOfWhite - 1
                    elif board[move[0] + 1][move[1] - 1] == " 2":
                        numberOfKingWhite = numberOfKingWhite - 1
                    board[move[0] + 1][move[1] - 1] = "__"
                board[move[0]][move[1]] = "__"

            # update w values
            w0 = w0 + (0.0001 * error)
            w1 = w1 + (0.0001 * error * numberOfBlack)
            w2 = w2 + (0.0001 * error * numberOfWhite)
            w3 = w3 + (0.0001 * error * numberOfKingBlack)
            w4 = w4 + (0.0001 * error * numberOfKingWhite)
            w5 = w5 + (0.0001 * error * black_in_danger_recognition(board))
            w6 = w6 + (0.0001 * error * white_in_danger_recognition(board))

    results.append(result)


print("w0 = %f, w1 = %f, w2 = %f, w3 = %f, w4 = %f, w5 = %f, w6 = %f" % (w0, w1, w2, w3, w4, w5, w6))
for i in range(500):
    sys.stdout.write(str(results[i]) + " , ")
    if i % 20 == 0:
        sys.stdout.write('\n')
import random


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def bot_choice(board, mark):
    bot_choice_list = []
    for i in range(0, len(board)):
        if board[i] == ' ':
            bot_choice_list.append(i)
    board[random.choice(bot_choice_list)] = mark


# main
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = 'Player 1'
    print('you will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        elif turn == 'Player 2':
            # Player2's turn.
            a = 0
            A = False
            B = False
            while a <= 0:
                A1 = board[8] == player2_marker and board[9] == player2_marker
                A2 = board[9] == player2_marker and board[6] == player2_marker
                A3 = board[4] == player2_marker and board[1] == player2_marker
                A4 = board[4] == player2_marker and board[1] == player2_marker
                A5 = board[7] == player2_marker and board[8] == player2_marker
                A6 = board[7] == player2_marker and board[4] == player2_marker
                A7 = board[1] == player2_marker and board[2] == player2_marker
                A8 = board[6] == player2_marker and board[3] == player2_marker
                B1 = board[7] == player2_marker and board[9] == player2_marker
                B2 = board[4] == player2_marker and board[6] == player2_marker
                B3 = board[1] == player2_marker and board[3] == player2_marker
                B4 = board[7] == player2_marker and board[1] == player2_marker
                B5 = board[9] == player2_marker and board[3] == player2_marker
                B6 = board[8] == player2_marker and board[2] == player2_marker
                B7 = board[7] == player2_marker and board[3] == player2_marker
                B8 = board[9] == player2_marker and board[1] == player2_marker
                C1 = board[5] == player2_marker and board[6] == player2_marker
                C2 = board[5] == player2_marker and board[4] == player2_marker
                C3 = board[5] == player2_marker and board[2] == player2_marker
                C4 = board[5] == player2_marker and board[8] == player2_marker
                C5 = board[5] == player2_marker and board[1] == player2_marker
                C6 = board[5] == player2_marker and board[3] == player2_marker
                C7 = board[5] == player2_marker and board[9] == player2_marker
                C8 = board[5] == player2_marker and board[7] == player2_marker
                if A1:
                    sp = space_check(board, 7)
                    if sp:
                        board[7] = player2_marker
                        A = True
                        break
                if A2:
                    sp = space_check(board, 3)
                    if sp:
                        board[3] = player2_marker
                        A = True
                        break
                if A3:
                    sp = space_check(board, 1)
                    if sp:
                        board[1] = player2_marker
                        A = True
                        break
                if A4:
                    sp = space_check(board, 7)
                    if sp:
                        board[7] = player2_marker
                        A = True
                        break
                if A5:
                    sp = space_check(board, 9)
                    if sp:
                        board[9] = player2_marker
                        A = True
                        break
                if A6:
                    sp = space_check(board, 1)
                    if sp:
                        board[1] = player2_marker
                        A = True
                        break
                if A7:
                    sp = space_check(board, 3)
                    if sp:
                        board[3] = player2_marker
                        A = True
                        break
                if A8:
                    sp = space_check(board, 9)
                    if sp:
                        board[9] = player2_marker
                        A = True
                        break
                if B1:
                    sp = space_check(board, 8)
                    if sp:
                        board[8] = player2_marker
                        A = True
                        break
                if B2:
                    sp = space_check(board, 5)
                    if sp:
                        board[5] = player2_marker
                        A = True
                        break
                if B3:
                    sp = space_check(board, 2)
                    if sp:
                        board[2] = player2_marker
                        A = True
                        break
                if B4:
                    sp = space_check(board, 4)
                    if sp:
                        board[4] = player2_marker
                        A = True
                        break
                if B5:
                    sp = space_check(board, 6)
                    if sp:
                        board[6] = player2_marker
                        A = True
                        break
                if B6:
                    sp = space_check(board, 5)
                    if sp:
                        board[5] = player2_marker
                        A = True
                        break
                if B7:
                    sp = space_check(board, 5)
                    if sp:
                        board[5] = player2_marker
                        A = True
                        break
                if B8:
                    sp = space_check(board, 5)
                    if sp:
                        board[5] = player2_marker
                        A = True
                        break
                if C1:
                    sp = space_check(board, 4)
                    if sp:
                        board[4] = player2_marker
                        A = True
                        break
                if C2:
                    sp = space_check(board, 6)
                    if sp:
                        board[6] = player2_marker
                        A = True
                        break
                if C3:
                    sp = space_check(board, 8)
                    if sp:
                        board[8] = player2_marker
                        A = True
                        break
                if C4:
                    sp = space_check(board, 2)
                    if sp:
                        board[2] = player2_marker
                        A = True
                        break
                if C5:
                    sp = space_check(board, 9)
                    if sp:
                        board[9] = player2_marker
                        A = True
                        break
                if C6:
                    sp = space_check(board, 7)
                    if sp:
                        board[7] = player2_marker
                        A = True
                        break
                if C7:
                    sp = space_check(board, 1)
                    if sp:
                        board[1] = player2_marker
                        A = True
                        break
                if C8:
                    sp = space_check(board, 3)
                    if sp:
                        board[3] = player2_marker
                        A = True
                        break
                # if A == False:
                #     bot_choice(board, player2_marker)
                #     break
                a += 1

            if A == False:
                b = 0
                while b <= 0:
                    A1 = board[8] == player1_marker and board[9] == player1_marker
                    A2 = board[9] == player1_marker and board[6] == player1_marker
                    A3 = board[4] == player1_marker and board[1] == player1_marker
                    A4 = board[4] == player1_marker and board[1] == player1_marker
                    A5 = board[7] == player1_marker and board[8] == player1_marker
                    A6 = board[7] == player1_marker and board[4] == player1_marker
                    A7 = board[1] == player1_marker and board[2] == player1_marker
                    A8 = board[6] == player1_marker and board[3] == player1_marker
                    B1 = board[7] == player1_marker and board[9] == player1_marker
                    B2 = board[4] == player1_marker and board[6] == player1_marker
                    B3 = board[1] == player1_marker and board[3] == player1_marker
                    B4 = board[7] == player1_marker and board[1] == player1_marker
                    B5 = board[9] == player1_marker and board[3] == player1_marker
                    B6 = board[8] == player1_marker and board[2] == player1_marker
                    B7 = board[7] == player1_marker and board[3] == player1_marker
                    B8 = board[9] == player1_marker and board[1] == player1_marker
                    C1 = board[5] == player1_marker and board[6] == player1_marker
                    C2 = board[5] == player1_marker and board[4] == player1_marker
                    C3 = board[5] == player1_marker and board[2] == player1_marker
                    C4 = board[5] == player1_marker and board[8] == player1_marker
                    C5 = board[5] == player1_marker and board[1] == player1_marker
                    C6 = board[5] == player1_marker and board[3] == player1_marker
                    C7 = board[5] == player1_marker and board[9] == player1_marker
                    C8 = board[5] == player1_marker and board[7] == player1_marker
                    if A1:
                        sp = space_check(board, 7)
                        if sp:
                            board[7] = player2_marker
                            B = True
                            break
                    if A2:
                        sp = space_check(board, 3)
                        if sp:
                            board[3] = player2_marker
                            B = True
                            break
                    if A3:
                        sp = space_check(board, 1)
                        if sp:
                            board[1] = player2_marker
                            B = True
                            break
                    if A4:
                        sp = space_check(board, 7)
                        if sp:
                            board[7] = player2_marker
                            B = True
                            break
                    if A5:
                        sp = space_check(board, 9)
                        if sp:
                            board[9] = player2_marker
                            B = True
                            break
                    if A6:
                        sp = space_check(board, 1)
                        if sp:
                            board[1] = player2_marker
                            B = True
                            break
                    if A7:
                        sp = space_check(board, 3)
                        if sp:
                            board[3] = player2_marker
                            B = True
                            break
                    if A8:
                        sp = space_check(board, 9)
                        if sp:
                            board[9] = player2_marker
                            B = True
                            break
                    if B1:
                        sp = space_check(board, 8)
                        if sp:
                            board[8] = player2_marker
                            B = True
                            break
                    if B2:
                        sp = space_check(board, 5)
                        if sp:
                            board[5] = player2_marker
                            B = True
                            break
                    if B3:
                        sp = space_check(board, 2)
                        if sp:
                            board[2] = player2_marker
                            B = True
                            break
                    if B4:
                        sp = space_check(board, 4)
                        if sp:
                            board[4] = player2_marker
                            B = True
                            break
                    if B5:
                        sp = space_check(board, 6)
                        if sp:
                            board[6] = player2_marker
                            B = True
                            break
                    if B6:
                        sp = space_check(board, 5)
                        if sp:
                            board[5] = player2_marker
                            B = True
                            break
                    if B7:
                        sp = space_check(board, 5)
                        if sp:
                            board[5] = player2_marker
                            B = True
                            break
                    if B8:
                        sp = space_check(board, 5)
                        if sp:
                            board[5] = player2_marker
                            B = True
                            break
                    if C1:
                        sp = space_check(board, 4)
                        if sp:
                            board[4] = player2_marker
                            B = True
                            break
                    if C2:
                        sp = space_check(board, 6)
                        if sp:
                            board[6] = player2_marker
                            B = True
                            break
                    if C3:
                        sp = space_check(board, 8)
                        if sp:
                            board[8] = player2_marker
                            B = True
                            break
                    if C4:
                        sp = space_check(board, 2)
                        if sp:
                            board[2] = player2_marker
                            B = True
                            break
                    if C5:
                        sp = space_check(board, 9)
                        if sp:
                            board[9] = player2_marker
                            B = True
                            break
                    if C6:
                        sp = space_check(board, 7)
                        if sp:
                            board[7] = player2_marker
                            B = True
                            break
                    if C7:
                        sp = space_check(board, 1)
                        if sp:
                            board[1] = player2_marker
                            B = True
                            break
                    if C8:
                        sp = space_check(board, 3)
                        if sp:
                            board[3] = player2_marker
                            B = True
                            break
                    if B == False:
                        bot_choice(board, player2_marker)
                        break
                b += 1

            # if A == False and B == False:
            #     c = 0
            #     while c <= 0:
            #         D1 =

            if win_check(board, player2_marker):
                display_board(board)
                print('Bot has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    game_on =False
                else:
                    turn = 'Player 1'

            B = False
    if not replay():
        break




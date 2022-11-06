

"""
圈叉遊戲
"""

import random


def main():
    while True:
        # choose the role of being 'X' or 'O' for the player and the computer
        player, computer = choose_letter()

        # decide who goes first
        turn = who_goes_first()
        print("The {} goes first.".format(turn))

        # the game starts
        board = [' '] * 10  # empty game board
        count = 0  # record the number of steps. If count equals 9 and cannot determine who wins, then the game is tie.

        # if the player goes first
        if turn == 'player':
            draw_board(board)
            while count <= 9 and who_wins(board, player, computer) == None:
                make_move(board, player, count)
                count += 1
                make_move_computer(board, computer, count)
                count += 1
                draw_board(board)
            if who_wins(board, player, computer) != None:
                if who_wins(board, player, computer) == player:
                    print("The player wins.")
                elif who_wins(board, player, computer) == computer:
                    print("The computer wins.")
            else:
                print("Tie.")

        # if the computer goes first
        else:
            while count <= 9 and who_wins(board, player, computer) == None:
                make_move_computer(board, computer, count)
                count += 1
                draw_board(board)
                make_move(board, player, count)
                count += 1
                draw_board(board)
            if who_wins(board, player, computer) != None:
                if who_wins(board, player, computer) == player:
                    print("The player wins.")
                elif who_wins(board, player, computer) == computer:
                    print("The computer wins.")
            else:
                print("Tie.")

        # ask whether the player want to continue the game. ('y' for yes, others for quitting the game)
        if play_again() != 'y':
            print("End of the game.")
            break


def choose_letter():  # the player decide the role of being 'X' or 'O'
    player = str(input("Do you want to be X or O ?")).upper()
    if player == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():  # randomly decide who goes first
    if random.randint(0, 1) == 0:
        return 'player'
    else:
        return 'computer'


def draw_board(board):  # draw the game board
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |   ")
    print("           ")


def make_move(board, player, count):  # the player can decide which place to put its role
    if count != 9:
        place = int(input("Which place do you want to put? (Please select 1~9):"))
        board[place] = player
        return board


def make_move_computer(board, computer, count):  # the computer decide which place to put its role (random)
    if count != 9:
        while True:
            place = random.randint(1, 9)
            while board[place] == 'X' or board[place] == 'O':
                place = random.randint(1, 9)
            board[place] = computer
            return board


def who_wins(board, player, computer):  # determine who wins
    for i in range(1, 10):
        if (board[1] == board[2] == board[3] == player) or (board[4] == board[5] == board[6] == player) or \
            (board[7] == board[8] == board[9] == player) or (board[1] == board[4] == board[7] == player) or \
            (board[2] == board[5] == board[8] == player) or (board[3] == board[6] == board[9] == player) or \
            (board[1] == board[5] == board[9] == player) or (board[3] == board[5] == board[7] == player):
            return player
        elif (board[1] == board[2] == board[3] == computer) or (board[4] == board[5] == board[6] == computer) or \
            (board[7] == board[8] == board[9] == computer) or (board[1] == board[4] == board[7] == computer) or \
            (board[2] == board[5] == board[8] == computer) or (board[3] == board[6] == board[9] == computer) or \
            (board[1] == board[5] == board[9] == computer) or (board[3] == board[5] == board[7] == computer):
            return computer


def play_again():  # ask if the player wants to play again
    again = str(input("Do you want to play again? (Press 'y' for yes , others for no.)")).lower()
    return again


if __name__ == '__main__':
    main()
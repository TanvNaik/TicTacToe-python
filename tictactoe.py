"""
Simple Tic-Tac-Toe game with keyboard number pad style
"""
def display_board(board):
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))
    print('---|---|---')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('---|---|---')
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('   |   |   ')


def player1_input(board):

    #Taking input from player 1

    p1 = 'wrong'
    acceptable_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while p1.isdigit() == False or p1 not in acceptable_range:
        p1 = input('Player 1\'s turn. Choose a position: ')
        if p1 not in acceptable_range:
            print("Invalid position")
        if p1.isdigit():
            if int(p1) not in board:
                print('Invalid move')
                p1='wrong'
            else:
                return int(p1)


def player2_input(board):

    # Taking input from player 2

    p2 = 'wrong'
    acceptable_range = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while p2.isdigit() == False or p2 not in acceptable_range:
        p2 = input('Player 2\'s turn. Choose a position: ')
        if p2 not in acceptable_range:
            print("Invalid position")
        if p2.isdigit():
            if int(p2) not in board:
                print('Invalid move')
                p2='wrong'
            else:
                return int(p2)


def update(board, position, player):

    # Updating the player's move

    if player == 1:
        board[position - 1] = 'X'
    elif player == 2:
        board[position - 1] = 'O'
    return board


def check(board):

    #Checking for winner

    if (board[6] == board[7] == board[8] or board[6] == board[4] == board[2] or board[6] == board[3] == board[0]):
        if board[6] == 'X':
            return 1
        else:
            return 2
    elif board[7] == board[4] == board[1]:
        if board[7] == 'X':
            return 1
        else:
            return 2
    elif board[8] == board[4] == board[0] or board[8] == board[5] == board[2]:
        if board[8] == 'X':
            return 1
        else:
            return 2
    elif board[3] == board[4] == board[5]:
        if board[3] == 'X':
            return 1
        else:
            return 2
    elif board[0] == board[1] == board[2]:
        if board[0] == 'X':
            return 1
        else:
            return 2

def draw(board):

    #Checking if it is a Draw

    temp=0
    for x in [1,2,3,4,5,6,7,8,9]:
        if x in board:
            temp+=1
    if temp==0:
        return 'Draw'
    else:
        return False

def gameon_check(board):

    #Check whether player wants to play again

    choice = 'Wrong'
    while choice not in ['yes', 'no']:
        choice = input('Keep playing?(yes or no): ')
        if choice not in ['yes', 'no']:
            print('Please choose y or n')

    if choice == 'y':
        board=[1,2,3,4,5,6,7,8,9]
        return True,board
    else:
        return False,board


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameon = True
while gameon:
    display_board(board)
    p1 = player1_input(board)
    update(board, p1, 1)
    display_board(board)
    tie = draw(board)
    winner = check(board)
    if winner==1:
        print('Player 1 won!')
        gameon,board = gameon_check(board)
        continue
    if winner==2:
        print('Player 2 won!')
        gameon,board = gameon_check(board)
        continue
    if tie == 'Draw':
        print('Game tied')
        gameon,board = gameon_check(board)
        continue
    p2 = player2_input(board)
    update(board, p2, 2)
    display_board(board)
    winner=check(board)
    tie=draw(board)
    if winner==1:
        print('Player 1 won!')
        gameon,board = gameon_check(board)
    if winner==2:
        print('Player 2 won!')
        gameon,board = gameon_check(board)
    if tie=='Draw':
        print('Game tied')
        gameon,board = gameon_check(board)
    print('\n' *50)
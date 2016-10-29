CONVERSION_TABLE = {'00': 0, '01': 1, '02': 2,
                    '10': 3, '11': 4, '12': 5,
                    '20': 6, '21': 7, '22': 8}

def homo_string(string):
    '''
    returns True if string consists of same characters
    returns False otherwise
    '''
    if string.count(string[0]) == len(string):
        return True
    else: 
        return False

def init_board():
    return "---------"

def update_board(player, position, board):
    '''
    player: X or O
    postion: position for a position xy
        use CONVERSION_TABLE to find position
    board: current board
    '''
    # num_postion = CONVERSION_TABLE[position]
    num_postion = position
    board = board[:num_postion] + board[num_postion:].replace('-', player, 1)
    return board

def print_board(board):
    '''
    print board
    '''
    for i in range(0,9,3):
        print(board[i:i+3])

def moves_left(board):
    '''
    returns possible moves left
    '''
    moves = []
    index = 0
    for i in board:
        if i == '-':
            moves.append(index)
        index += 1
    return moves

def check_board(board):
    '''
    checks if one player has won
    '''
    # check if board full 
    if moves_left(board) == []:
        return 'Draw'
    
    # check vertical and horizontal
    for i in [0,3,6]:
        j = int(i/3)
        if homo_string(board[i:i+3]):
            return board[i]
        elif homo_string(board[j] + board[j + 3] + board[j +6]):
            return board[j]
        else:
            continue

    # check diagonal
    if homo_string(board[0] + board[4] + board[8]):
        return board[0]
    elif homo_string(board[2] + board[4] + board[6]):
        return board[2]
    else:
        return '-'

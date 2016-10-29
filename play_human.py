import tic.first as t
import random

def play():
    # Initialize board
    board = t.init_board()
    print('Lets Begin!\n')
    t.print_board(board)
    
    # Initialize temp variables
    num_moves = 0
    winner = 'Draw'
    while num_moves < 10:
        # input1
        print('Move X')
        
        # get possible moves left 
        moves = t.moves_left(board)
        
        # chose a move and update board
        board = t.update_board('X', moves[random.randint(0,len(moves) - 1)], board)
        t.print_board(board)
        
        # check if game won
        print('')
        if t.check_board(board) != '-':
            winner = t.check_board(board)
            break
        
        # input2
        print('Move O')
        
        # get possible moves left 
        moves = t.moves_left(board)
        
        # chose a move and update board
        board = t.update_board('O', int(input('Enter location: ')), board)
        t.print_board(board)
        
        # check if game won
        print('')
        if t.check_board(board) != '-':
            winner = t.check_board(board)
            break
        
        # Increment number of moves
        num_moves += 2
    
    print(winner)


if __name__ == "__main__":
    play()
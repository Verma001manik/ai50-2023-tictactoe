"""
Tic Tac Toe Player
"""

import math
import copy 


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    TURN = None
    xcount = 0 
    ocount = 0

    if not terminal(board):
        for i in range(3):
            for j in range(3):
            # if board[i][j] == EMPTY:
            #     TURN = X
            #     break
                if board[i][j] == X:
                    xcount+= 1
                elif board[i][j] == O:
                    ocount += 1 
                else:
                    pass
        if xcount > ocount:
            TURN = O
            return TURN 
        else: 

        
            TURN = X
            return TURN 
    
    
    
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                # print(i,j)
                empty_cells.append((i, j))
                

    return empty_cells
                
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newboard = copy.deepcopy(board)
    # print(newboard)

    if action in actions(board):
        # print(f"action: ", action)
        
        res = player(board=board)
        for i in range(3):
            for j in range(3):
                if i==action[0] and j==action[1]:
                    newboard[i][j] = res
                    break
        # print("new board: ",newboard)
        return newboard

    else:
        raise Exception("not empty")
    # print(action)
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if terminal(board):
        win = None
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                win =  row[0]

    # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                win =  board[0][col]

    # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            win = board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            win =  board[0][2] 
        # print("winner: ",win)
        return win 

    


# Everything works fine till the winner function 
# def terminal(board):
#     """
#     Returns True if game is over, False otherwise.
#     """
#     count = 0 
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] != None:
                
#                 return True
                
#             else: 
#                 count +=1 
#                 print("count: ", count)
#                 return False 
def terminal(board):
    """
    Returns True if the game is over (win or draw), False otherwise.
    """
    return all(cell is not None for row in board for cell in row)



# everything is good till terminal too 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if terminal(board):
        if winner(board) == 'X':
            return  1 
        elif winner(board) == 'O':
            return  -1
        else: 
            return 0 
   

# everything is good too till utility
   
def maxvalue(board):
    # Check if the game is over (terminal state)
    if terminal(board):
        return utility(board)
    
    v = float("-inf")  # Initialize v to negative infinity
    
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    
    return v

def minvalue(board):
    # Check if the game is over (terminal state)
    if terminal(board):
        return utility(board)
    
    v = float("inf")  # Initialize v to positive infinity
    
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    
    return v


def minimax(board):
    if player(board) == 'X':
        # Maximizing player's turn
        best_value = float("-inf")
        best_action = None
        for action in actions(board):
            current_value = minvalue(result(board, action))
            if current_value > best_value:
                best_value = current_value
                best_action = action
        return best_action
    else:
        # Minimizing player's turn
        best_value = float("inf")
        best_action = None
        for action in actions(board):
            current_value = maxvalue(result(board, action))
            if current_value < best_value:
                best_value = current_value
                best_action = action
        return best_action


    # raise NotImplementedError
tic_tac_toe_board1 = [

    [EMPTY, O, X],
    [EMPTY, EMPTY,O],
    [X, X, EMPTY]
]
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'X', 'O']
]
# print(player(tic_tac_toe_board))
# print(player(tic_tac_toe_board1))
# print(actions(tic_tac_toe_board))
# print(actions(tic_tac_toe_board1))


# result(tic_tac_toe_board1, (1,1))
# winner(tic_tac_toe_board)
# winner(tic_tac_toe_board)
# print(utility(tic_tac_toe_board))
# print(utility(tic_tac_toe_board))
# print(terminal(tic_tac_toe_board))
# print(terminal(tic_tac_toe_board1))
# print(minimax(tic_tac_toe_board))
# print(minimax(tic_tac_toe_board1))
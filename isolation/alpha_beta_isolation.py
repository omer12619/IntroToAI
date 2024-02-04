import math

#helper function to manage this hard thing that i try to understand
def alphabeta_max(current_game):
    return alphabeta_maxmin(current_game,-math.inf,math.inf)

# another helper function to manage this hard thing that i try to understand
def alphabeta_min(current_game):
    return alphabeta_minmax(current_game,-math.inf,math.inf)



def alphabeta_maxmin(current_game,alpha,beth):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    best_move = None
    for move in moves:
        mx, next_move = alphabeta_minmax(move,alpha,beth)

        if v < mx:
            v = mx
            best_move = move
        beth =min(beth,v)

        if beth <= alpha :
            break

        #add code here for alpha-beta algorithm
    return v, best_move


def alphabeta_minmax(current_game,alpha,beth):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    best_move = None
    for move in moves:
        mx, next_move = alphabeta_maxmin(move,alpha,beth)
        alpha=max(alpha,mx)

        if v > mx:
            v = mx
            best_move = move
        if (beth <= alpha):
            break
        #add code here for alpha-beta algorithm
    return v, best_move

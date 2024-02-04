import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    return alphabeta_maxmin_h(current_game, -math.inf, math.inf,depth)



def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # add code here
    return alphabeta_minimax_h(current_game, -math.inf, math.inf,depth)



def alphabeta_maxmin_h(current_game,alpha,beth, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    best_move = None
    for move in moves:

        mx, next_move = alphabeta_minimax_h(move, alpha, beth,depth-1)

        if v < mx:
            v = mx
            best_move = move
        beth = min(beth, v)

        if beth <= alpha:
            break

        # add code here for alpha-beta algorithm
    return v, best_move


def alphabeta_minimax_h(current_game,alpha,beth, depth):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    best_move = None
    for move in moves:
        mx, next_move = alphabeta_maxmin_h(move, alpha, beth,depth-1)
        alpha = max(alpha, mx)

        if v > mx:
            v = mx
            best_move = move
        if (beth <= alpha):
            break
        # add code here for alpha-beta algorithm
    return v, best_move





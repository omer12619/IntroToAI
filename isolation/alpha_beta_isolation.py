import math


def alphabeta_max(current_game):
    #add code here for alpha-beta
    pass

def alphabeta_min(current_game):
    #add code here for alpha-beta
    pass


def maximin(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move)
        if v < mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move


def minimax(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move)
        if v > mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
    return v, best_move

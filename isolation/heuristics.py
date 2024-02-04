import game_state



def calculate_potential_moves (game_state, player=None):

        moves = []
        curr_player = player if player is not None else game_state.get_curr_player()
        curr_location = game_state.get_player_locations()[curr_player]


        for i in range(-1, 2):
            for j in range(-1, 2):
                game_state.add_moves_in_direction(curr_location, (i, j), moves)

        return moves



def base_heuristic(game_state):



        player1_moves = len(calculate_potential_moves(game_state, player=1))
        player2_moves = len(calculate_potential_moves(game_state, player=2))

        return player1_moves - player2_moves

def advanced_heuristic(curr_state):
        return 0

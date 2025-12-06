from isoKnight.game_state import game_state


def base_heuristic(curr_state):  # curr_state is a Game state

    # add code here
    curr_player = curr_state.get_curr_player()
    locations = curr_state.get_player_locations()

    if curr_player == 1:
        moves_for_player1 = len(curr_state.potential_moves())
        temp_state = game_state(curr_state.get_grid().copy(), locations[1], locations[2], 2)
        moves_for_player2 = len(temp_state.potential_moves())

    else:
        moves_for_player2 = len(curr_state.potential_moves())
        temp_state = game_state(curr_state.get_grid().copy(), locations[1], locations[2], 1)
        moves_for_player1 = len(temp_state.potential_moves())

    return moves_for_player1 - moves_for_player2


def advanced_heuristic(curr_state):
    return 0

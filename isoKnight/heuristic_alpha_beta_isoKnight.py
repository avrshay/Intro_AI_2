import math

h = None


def alphabeta_max_h(current_game, _heuristic, depth=3):  # warrper func fot the recursive func
    global h
    h = _heuristic
    # add code here

    # initializing variables for recursive
    return maximin(current_game, depth, -math.inf, math.inf)


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # add code here

    # initializing variables for recursive
    return minimax(current_game, depth, -math.inf, math.inf)


def maximin(current_game, depth, alpha, beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    best_move = None

    for move in moves:
        mx, next_move = minimax(move, depth - 1, alpha, beta)
        if best_move is None or v < mx:
            v = mx
            best_move = move

        alpha = max(v, alpha)
        if beta <= alpha:
            return v, None  # don't choose this way

    return v, best_move


def minimax(current_game, depth, alpha, beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None  # stop condition
    if depth == 0:
        return h(current_game), None
        # reach to the maximum search depth -Time and memory limit, so we return the v=h instead
    v = math.inf
    moves = current_game.get_moves()
    best_move=None

    for move in moves:
        mx, next_move = maximin(move, depth - 1, alpha, beta)
        if best_move is None or v > mx:
            v = mx
            best_move = move

        beta = min(v, beta)
        if beta <= alpha:  # there is no point in continuing this path:
            return v, None  # don't choose this way

    return v, best_move

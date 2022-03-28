for s in all states:

    best_utility = -inf
    best_move = None
    for all actions on s => s':
        utility = 0
        for all states:
            utility += T(s', s) * U(s')

        if utility > best_utility:
            best_utility = utility
            best_move = action

    utility(s) = best_utility + instant reward
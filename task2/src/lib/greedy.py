def greedy(n, m, p, r, b):
    """solve the problem with the greedy algorithm (Not always the optimal solution)

    Args:
        n (int): number of items
        m (int): number of restrictions
        p (list): list of prices
        r (list): list of restrictions
        b (list): list of budgets

    Returns:
        int: the maximum price under the restrictions
    """
    p_with_index = [(p[i], i) for i in range(n)]
    p_with_index.sort(reverse=True)
    opt = 0
    for p_index in range(n):
        for i in range(m):
            if r[i][p_index] > b[i]:
                break
        else:
            for i in range(m):
                b[i] -= r[i][p_index]
            opt += p[p_index]
    return opt


def greedy2(n, m, p, r, b, item_flag):
    opt = 0
    return opt
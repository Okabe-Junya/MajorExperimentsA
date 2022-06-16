import heapq

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
    sort_p = sorted(p, reverse=True)
    opt = 0
    for i in range(n):
        if item_flag[i] == 1:
            opt += p[i]
            for j in range(m):
                b[j] -= r[j][i]
    
    for i in range(n):
        max_p = sort_p[i]
        if p.index(max_p) != -1:
            continue
        item_flag[i] = 1
        for j in range(m):
            if r[j][i] > b[j]:
                break
        else:
            for j in range(m):
                b[j] -= r[j][i]
                opt += max_p
    return opt
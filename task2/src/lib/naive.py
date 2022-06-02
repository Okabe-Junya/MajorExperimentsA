import time

def naive(n, m, p, r, b):
    """solve the problem with the naive full bit search

    Args:
        n (int): number of items
        m (int): number of restrictions
        p (list): list of prices
        r (list): list of restrictions
        b (list): list of budgets

    Returns:
        int: the maximum price under the restrictions
    """
    executable_solution = []
    start_time = time.time()
    for num in range(2 ** n):
        tmp_time = time.time()
        if tmp_time - start_time > 2.0:
            return -1 # timeout

        choice = []
        check = [0] * m
        bin_num = str(bin(num)[2:]).zfill(n)

        assert len(bin_num) == n

        for bit in range(n):
            if bin_num[bit] == '1':
                choice.append(p[bit])
                for item in range(m):
                    check[item] += r[item][bit]

        for item in range(m):
            if check[item] > b[item]:
                break
        else:
            executable_solution.append(sum(choice))
    return max(executable_solution)
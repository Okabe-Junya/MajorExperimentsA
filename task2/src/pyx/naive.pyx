def naive(n: int, m: int, p: list, r: list, b: list):
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

    cdef:
        list executable_solution, choice, check
        int num, bit, item
        str bit_num
    executable_solution = []
    for num in range(2 ** n):
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
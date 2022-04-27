import sys
import time

from input import parse_input


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


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = naive(n, m, p, r, b)
    time_end = time.time()

    assert res == opt
    print("Minimum price:", res)
    print("Time: {:.3f}sec".format(time_end - time_start))


if __name__ == '__main__':
    main()

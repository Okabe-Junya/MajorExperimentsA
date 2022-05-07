import sys
import time

from input import parse_input


def branch_and_bound(n, m, p, r, b):
    """solve the problem with the branch and bound algorithm

    Args:
        n (int): number of items
        m (int): number of restrictions
        p (list): list of prices
        r (list): list of restrictions
        b (list): list of budgets

    Returns:
        int: the maximum price under the restrictions
    """

    opt = 0
    return opt


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = branch_and_bound(n, m, p, r, b)
    time_end = time.time()

    assert res == opt
    print("Minimum price:", res)
    print("Time: {:.3f}sec".format(time_end - time_start))


if __name__ == '__main__':
    main()

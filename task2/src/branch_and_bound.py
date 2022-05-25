import sys
import time
from collections import deque
import pulp

from lib.input import parse_input
from lib.greedy import greedy
from lib.liner import liner


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

    init_opt = greedy(n, m, p, r, b.copy())
    part_prob = deque()
    part_prob.append((n, m, p, r, b))
    while part_prob:
        # TODO: 部分問題を取り出し，分枝限定の実装を行う
        tmp_prob = part_prob.popleft()
        res = liner(*tmp_prob)
    return res


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = branch_and_bound(n, m, p, r, b)
    time_end = time.time()

    # assert res == opt
    print("Max price:", res)
    print("Time: {:.3f}sec".format(time_end - time_start))


if __name__ == '__main__':
    main()

from re import M
import sys
import time
from collections import deque

from lib.input import parse_input
from lib.greedy import greedy
from lib.liner import liner_with_solver, liner_with_simplex

def make_subtree_problem(n, m, p, r, b):
    """make two subtree problems
    
    Args:
        n (int): number of items
        m (int): number of restrictions
        p (list): list of prices
        r (list): list of restrictions
        b (list): list of budgets

    Returns:
        list: list of subtree problems(len = 2)
    """
    p1 = [p[i] for i in range(n - 1)]
    r1 = [[r[i][j] for j in range(n - 1)] for i in range(m)]
    b1 = [(b[i] - r[i][-1]) for i in range(m)]
    b2 = [b[i] for i in range(m)]
    prob1 = (n - 1, m - 1, p1, r1, b1, True)
    prob2 = (n - 1, m - 1, p1, r1, b2, False)
    return [prob1, prob2]


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

    tmp_opt = greedy(n, m, p, r, b.copy())
    ans_list = [-1] * n
    part_prob = deque()
    part_prob.append((n, m, p, r, b, ans_list))
    while part_prob:
        tmp_prob = part_prob.popleft()
        if DEBUG:
            res = liner_with_solver(*tmp_prob[:-1])
        else:
            res = liner_with_simplex(*tmp_prob[:-1])
        print("res:", res)
        if res < tmp_opt:
            continue
        else:
            tmp_opt = res
            new_prob1, new_prob2 = make_subtree_problem(*tmp_prob[:-1])
            part_prob.append(new_prob1)
            part_prob.append(new_prob2)
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
    DEBUG = True
    main()
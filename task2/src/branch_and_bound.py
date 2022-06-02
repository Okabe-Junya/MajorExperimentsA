import sys
import time
from collections import deque

from lib.input import parse_input
from lib.greedy import greedy
from lib.liner import liner_with_solver, liner_with_simplex


def make_subtree_problem(n, m, p, r, b, item_flag):
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

    item_flag1 = item_flag.copy()
    item_flag1[n - 1] = 1
    item_flag2 = item_flag.copy()
    item_flag2[n - 1] = 0

    for num in range(m):
        if b1[num] < 0:
            b1 = -1
            break
    for num in range(m):
        if b2[num] < 0:
            b2 = -1
            break
    prob1 = (n - 1, m - 1, p1, r1, b1, item_flag1)
    prob2 = (n - 1, m - 1, p1, r1, b2, item_flag2)
    return [prob1, prob2]


def check_subject(r, b, x):
    for i in range(len(r)):
        tmp_sum = 0
        for j in range(len(r[i])):
            tmp_sum +=  r[i][j] * x[j]
        if tmp_sum > b[i]:
            return False
    return True


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
    r_init = r.copy()
    b_init = b.copy()
    tmp_opt = greedy(n, m, p, r, b.copy())
    item_flag = [-1] * n
    ans_list = []
    part_prob = deque()
    part_prob.append((n, m, p, r, b, item_flag))
    while part_prob:
        tmp_prob = part_prob.popleft()
        if -1 not in tmp_prob[-1]:
            if check_subject(r_init, b_init, tmp_prob[-1]):
                ans_list.append(tmp_prob[-1])
        if DEBUG:
            res = liner_with_solver(*tmp_prob[:-1])
            if res is None:
                continue
        else:
            res = liner_with_simplex(*tmp_prob[:-1])
        tmp_sum = 0
        for i in range(n):
            if tmp_prob[-1][i] == 1:
                tmp_sum += p[i]
        if res + tmp_sum < tmp_opt:
            continue
        else:
            tmp_opt = tmp_sum
            new_prob1, new_prob2 = make_subtree_problem(*tmp_prob)
            if not new_prob1[4] == -1:
                part_prob.append(new_prob1)
            if not new_prob2[4] == -1:
                part_prob.append(new_prob2)

    opt = 0
    for ans in ans_list:
        tmp_sum = 0
        for i in range(n):
            if ans[i] == 1:
                tmp_sum += p[i]
        if tmp_sum > opt:
            opt = tmp_sum
    return opt


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

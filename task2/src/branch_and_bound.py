import sys
import time
from collections import deque
import pulp

from input import parse_input


def liner_programing(n, m, p, r, b):
    prob = pulp.LpProblem("linear_relaxation", pulp.LpMaximize)
    # 変数の定義
    xj = [pulp.LpVariable("x{}".format(j), lowBound=0,
                          upBound=1, cat='Integer') for j in range(n)]
    
    # 目的関数の設定
    prob += pulp.lpDot(p, xj)
    
    # 制約条件の設定
    for i in range(n):
        prob += pulp.lpDot(r[i], xj) <= b[i]
    
    # 最適化問題を解く
    status = prob.solve()
    return prob.objective.value()


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

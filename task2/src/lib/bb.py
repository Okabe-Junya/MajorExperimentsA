import sys
import time
from collections import deque

from lib.input import parse_input
from lib.greedy import greedy, greedy2
from lib.liner import liner_with_solver
from lib.simplex import simplex


def make_subtree_problem(r, b, item_flag):
    prob1_flag = item_flag.copy()
    prob2_flag = item_flag.copy()
    for i in range(len(item_flag), 0, -1):
        if item_flag[i - 1] == -1:
            prob1_flag[i - 1] = 0
            prob2_flag[i - 1] = 1
            if not check_subject(r, b, prob2_flag):
                prob2_flag = None
            return prob1_flag, prob2_flag
    return None, None


def check_subject(r, b, x):
    for i in range(len(r)):
        tmp_sum = 0
        for j in range(len(r[i])):
            if x[j] == -1:
                continue
            tmp_sum += r[i][j] * x[j]
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
    
    # 初期値の設定
    """
    pr = [p] + r
    pr_T = [list(t) for t in zip(*pr)]
    pr_T.sort()
    pr = [list(t) for t in zip(*pr_T)]
    p = pr.pop(0)
    r_init = pr
    tmp_opt = greedy(n, m, p, r_init, b.copy()) # 暫定解
    """
    tmp_opt = 2400
    r_init = r
    

    start_time = time.time()
    item_flag = [-1] * n
    prob_queue = deque()
    prob_queue.append(item_flag)
    
    # 分枝限定法（幅優先探索）
    while prob_queue: # 部分問題がキューにある間
        # print(prob_queue)
        tmp_time = time.time()
        if tmp_time - start_time > 10.0:
            raise TimeoutError(
                "A timeout occurs because a single test case took more than 10 seconds"
            )

        tmp_prob = prob_queue.popleft() 
        if -1 not in tmp_prob: # 全てのitemが選択された場合
            if check_subject(r_init, b, tmp_prob):
                tmp_opt = max(tmp_opt, sum(p[i] * tmp_prob[i] for i in range(n)))
            continue
            
        ub = liner_with_solver(n, m, p, r_init, b, tmp_prob) # 線形緩和問題で上界を求める
        # TODO: greedy法による下界の計算
        lb = greedy2(n, m, p.copy(), r_init.copy(), b.copy(), tmp_prob)
        
        # 最適値を更新できないとわかったらそれ以上分岐しない
        if ub <= tmp_opt:
            continue
        
        if lb >= tmp_opt:
            tmp_opt = lb
        
        part_prob1, part_prob2 = make_subtree_problem(r, b, tmp_prob)
        
        if (part_prob1 is None) and (part_prob2 is None):
            continue
        elif part_prob1 is None:
            prob_queue.append(part_prob2)
            continue
        elif part_prob2 is None:
            prob_queue.append(part_prob1)
            continue
        
        if ub >= lb:
            prob_queue.append(part_prob1)
            prob_queue.append(part_prob2)
    
    return tmp_opt


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = branch_and_bound(n, m, p, r, b)
    time_end = time.time()

    assert res == opt
    print("Max price:", res)
    print("Time: {:.4f}sec".format(time_end - time_start))


if __name__ == '__main__':
    DEBUG = True
    main()

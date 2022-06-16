import pulp


def liner_with_solver(n, m, p, r, b, item_flag):
    """線形緩和問題をpulpを使って解く．元の問題の上界を計算する．
    
    Args:
        n (int): number of items
        m (int): number of restrictions
        p (list): list of prices
        r (list): list of restrictions
        b (list): list of budgets
    
    Returns:
        int: 緩和問題の最適値
    """
    prob = pulp.LpProblem("linear_relaxation", sense=pulp.LpMaximize)
    # 変数の定義
    xj = [pulp.LpVariable("x{}".format(j), lowBound=0,
                          upBound=1) for j in range(n)]
    # 目的関数の設定
    prob += pulp.lpDot(p, xj)
    # 制約条件の設定
    for i in range(m):
        prob += pulp.lpDot(r[i], xj) <= b[i]
    
    for i in range(n):
        if item_flag[i] != -1:
            prob += xj[i] == item_flag[i]

    # 最適化問題を解く
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    if prob.status:
        return prob.objective.value()
    else:
        return None
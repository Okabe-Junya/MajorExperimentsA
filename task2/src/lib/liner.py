import pulp


def liner_with_solver(n, m, p, r, b):
    prob = pulp.LpProblem("linear_relaxation", sense=pulp.LpMaximize)
    # 変数の定義
    xj = [pulp.LpVariable("x{}".format(j), lowBound=0,
                          upBound=1) for j in range(n)]
    # 目的関数の設定
    prob += pulp.lpDot(p, xj)
    # 制約条件の設定
    for i in range(m):
        prob += pulp.lpDot(r[i], xj) <= b[i]

    # print(prob)
    # 最適化問題を解く
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    if prob.status:
        return prob.objective.value()
    else:
        return 0


def liner_with_simplex(n, m, p, r, b):
    pass
import pulp

def liner(n, m, p, r, b):
    prob = pulp.LpProblem("linear_relaxation", sense=pulp.LpMaximize)
    # 変数の定義
    xj = [pulp.LpVariable("x{}".format(j), lowBound=0,
                          upBound=1) for j in range(n)]

    # 目的関数の設定
    prob += pulp.lpDot(p, xj)

    # 制約条件の設定
    for i in range(n):
        prob += pulp.lpDot(r[i], xj) <= b[i]

    #print(prob)
    # 最適化問題を解く
    prob.solve()
    if prob.status:
        return prob.objective.value()
    else:
        return 0
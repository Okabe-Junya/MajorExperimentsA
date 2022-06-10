import sys

import gurobipy as gp

from lib.input import parse_input


def solve(n, m, p, r, b):
    res = 0
    prob = gp.Model("knapsack_problem")
    prob.params.LogToConsole = 0  # ログを標準出力に出力しない

    var_list = []

    # 変数の定義
    for num in range(n):
        var_list.append(prob.addVar(
            vtype=gp.GRB.BINARY, name="var_{}".format(num)))

    # 制約条件の追加
    for i in range(m):
        prob.addConstr(
            gp.quicksum([var_list[j] * r[i][j] for j in range(n)]) <= b[i]
        )

    # 目的関数の設定
    prob.setObjective(gp.quicksum(p[i] * var_list[i]
                      for i in range(n)), gp.GRB.MAXIMIZE)

    # 最適化の実行
    prob.optimize()

    if prob.status == gp.GRB.OPTIMAL:  # 最適解が存在する場合
        res = prob.objVal
    else:
        res = None
    return res


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    res = solve(n, m, p, r, b)
    if res is not None:
        assert opt == res, "Expected {} but got {}".format(opt, res)
        print("Success! Optimal value: {}".format(res))
    else:
        print("No solution found")
        exit(1)


if __name__ == "__main__":
    main()

import gurobipy as gp


def solve(n: int, array: list) -> bool:
    """solve the bomber problem

    Args:
        n (int): number of squares on the board
        array (list): list of bomb numbers

    Returns:
        bool: True if feasible solution exists else False
    """
    
    # モデルの作成
    model = gp.Model("solve_bomber_puzzle")

    A = {}

    # 変数の定義
    for i in range(n + 2):
        for j in range(n + 2):
            A[i, j] = model.addVar(vtype=gp.GRB.BINARY,
                                   name="A[{},{}]".format(i, j))

    # 制約条件の追加
    for i in range(n + 2):
        for j in range(n + 2):
            # 境界は0である制約
            if (i == 0 or i == n + 1 or j == 0 or j == n + 1):
                model.addConstr(A[i, j] == 0)
                continue
            
            # ボムの数に関する制約
            if array[i][j] != 0:
                model.addConstr(A[i, j] == 0)
                model.addConstr(
                    gp.quicksum([A[i - 1, j - 1] + A[i - 1, j] + A[i - 1, j + 1] 
                                + A[i, j - 1] + A[i, j] + A[i, j + 1] 
                                + A[i + 1, j - 1] + A[i + 1, j] + A[i + 1, j + 1]]) 
                    == array[i][j]
                    )

    # 目的関数の設定（ダミー）
    model.setObjective(1, gp.GRB.MINIMIZE)

    # 最適化の実行
    model.optimize()
    
    # 結果の出力
    return(model.Status == gp.GRB.OPTIMAL)
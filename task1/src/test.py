import gurobipy as gp

from make_array import make_array
from solve import solve
from test_module.generate_random_true import generate_random_true


def main():
    # test_case1
    # 全ての要素が0の配列
    N = 10
    array = [[0] * (N + 2) for _ in range(N + 2)]
    res = solve(N, array)
    assert res

    # test_case2
    for _ in range(10):
        N, array = generate_random_true()
        res = solve(N, array)
        assert res

if __name__ == "__main__":
    main()

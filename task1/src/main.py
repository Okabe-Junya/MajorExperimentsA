import sys

import gurobipy as gp

from make_array import make_array
from solve import solve

def main():
    N = int(sys.argv[1])
    array = make_array(N)
    solve(N, array)


if __name__ == "__main__":
    main()

import sys
import time


from lib.input import parse_input
from lib.solver import solve
from lib.naive import naive
from lib.bb import branch_and_bound
from lib.liner import liner_with_solver


def main():
    solution_method = sys.argv[1]
    try:
        solution_method = int(solution_method)
    except ValueError:
        pass
    for i in range(1, 8):
        fname = "./test_case/case{}.txt".format(i)
        n, m, opt, p, r, b = parse_input(fname)

        if solution_method == 1:
            start_time_ns = time.perf_counter_ns()
            res = solve(n, m, p, r, b)
            end_time_ns = time.perf_counter_ns()
            assert opt == res, "Expected {} but got {}".format(opt, res)

        elif solution_method == 2:
            start_time_ns = time.perf_counter_ns()
            res = naive(n, m, p, r, b)
            end_time_ns = time.perf_counter_ns()
            assert opt == res, "Expected {} but got {}".format(opt, res)
        
        elif solution_method == 3:
            start_time_ns = time.perf_counter_ns()
            res = branch_and_bound(n, m, p, r, b)
            end_time_ns = time.perf_counter_ns()
            assert opt == res, "Expected {} but got {}".format(opt, res)
        
        else:
            print("Invalid solution method")
            exit(1)
        
        time_sec = (end_time_ns - start_time_ns) / 1e9
        print(time_sec, "sec")
        
    exit(0)

if __name__ == "__main__":
    main()
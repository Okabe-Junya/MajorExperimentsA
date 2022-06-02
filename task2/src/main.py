import sys
import time

from lib.input import parse_input
from lib.greedy import greedy
from lib.naive import naive
from lib.bb import branch_and_bound

def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = branch_and_bound(n, m, p, r, b)
    time_end = time.time()

    assert res == opt
    print("Minimum price:", res)
    print("Time: {:.3f}sec".format(time_end - time_start))

if __name__ == "__main__":
    main()

import sys

from lib.input import parse_input
from lib.greedy import greedy

def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    res = greedy(n, m, p, r, b)
    print(res, opt)


if __name__ == '__main__':
    main()
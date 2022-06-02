import sys
import time

from lib.input import parse_input
from lib.naive import naive
from pyx.naive import naive as naive_pyx


def test():
    for i in range(1, 8):
        fname = 'test_case/case' + str(i) + '.txt'
        n, m, opt, p, r, b = parse_input(fname)
        res = naive(n, m, p, r, b)
        if res == -1:
            print('timeout')
            continue
        assert res == opt

def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    time_start = time.time()
    res = naive(n, m, p, r, b)
    time_end = time.time()
    
    n, m, opt, p, r, b = parse_input(fname)
    time_start_pyx = time.time()
    res_pyx = naive(n, m, p, r, b)
    time_end_pyx = time.time()

    assert res ==  res_pyx ==opt 
    print("Minimum price:", res)
    print("Time: {:.3f}sec".format(time_end - time_start))
    print("Time(pyx): {:.3f}sec".format(time_end_pyx - time_start_pyx))


if __name__ == '__main__':
    main()


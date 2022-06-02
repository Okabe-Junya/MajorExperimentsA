import sys
import time

from lib.input import parse_input
from lib.naive import naive


def test():
    for i in range(1, 8):
        fname = 'test_case/case' + str(i) + '.txt'
        n, m, opt, p, r, b = parse_input(fname)
        res = naive(n, m, p, r, b)
        if res == -1:
            print('timeout')
            continue
        assert res == opt
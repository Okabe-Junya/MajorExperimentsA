from lib.input import parse_input
from lib.greedy import greedy

def test():
    for i in range(1, 8):
        fname = 'test_case/case' + str(i) + '.txt'
        n, m, opt, p, r, b = parse_input(fname)
        res = greedy(n, m, p, r, b)
        assert 0 <= res <= opt
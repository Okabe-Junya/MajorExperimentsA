from branch_and_bound import branch_and_bound
from lib.input import parse_input

def test():
    for i in range(1, 8):
        fname = 'test_case/case' + str(i) + '.txt'
        n, m, opt, p, r, b = parse_input(fname)
        res = naive(n, m, p, r, b)
        if res == -1:
            print('timeout')
            continue
        assert res == opt
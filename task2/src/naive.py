import sys

from input import parse_input


def naive(n, m, p, r, b):
    l = []
    for num in range(2 ** n):
        choice = []
        check = [0] * m
        bin_num = str(bin(num)[2:]).zfill(n)

        assert len(bin_num) == n

        for bit in range(n):
            if bin_num[bit] == '1':
                choice.append(p[bit])
                for item in range(m):
                    check[item] += r[item][bit]

        for item in range(m):
            if check[item] > b[item]:
                break
        else:
            l.append(sum(choice))
    return max(l)


def main():
    fname = sys.argv[1]
    n, m, opt, p, r, b = parse_input(fname)
    print(naive(n, m, p, r, b))


if __name__ == '__main__':
    main()

from input import parse_input


def main():
    for i in range(1, 8):
        n, m, opt, r, b = parse_input('./test_case/case{}.txt'.format(i))


if __name__ == "__main__":
    main()

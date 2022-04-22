def parse_input(input_file):
    """
    Parses the input file and returns a list of the lines.
    """

    with open(input_file, 'r') as f:
        r = []
        n, m, opt = [float(x) for x in f.readline().split()]
        n, m = int(n), int(m)
        for _ in range(int(m)):
            r_tmp = [float(x) for x in f.readline().split()]
            r.append(r_tmp)
        b = [int(x) for x in f.readline().split()]
    return n, m, opt, r, b

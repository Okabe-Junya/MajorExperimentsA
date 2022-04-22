from random import randint


def generate_random_true():
    """Generate a random board (guaranteed a solution exists.).

    Returns:
        array: The initial board (all boundary values are 0), size (n + 2) x (n + 2)
    """

    N = randint(10, 20)  # 1辺の長さ
    bomb_num = randint(5, 10)  # ボムの数
    bomb_map = [[False] * (N + 2) for _ in range(N + 2)]
    array = [[0] * (N + 2) for _ in range(N + 2)]

    # generate bomb randomly
    for _ in range(N):
        x, y = randint(1, N), randint(1, N)
        bomb_map[x][y] = True

    # generate bomb number
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if bomb_map[i][j]:
                array[i][j] = 0
            else:
                array[i][j] = sum([bomb_map[i - 1][j - 1] + bomb_map[i - 1][j] + bomb_map[i - 1][j + 1]
                                  + bomb_map[i][j - 1] +
                                   bomb_map[i][j] + bomb_map[i][j + 1]
                                  + bomb_map[i + 1][j - 1] + bomb_map[i + 1][j] + bomb_map[i + 1][j + 1]])

    return N, array

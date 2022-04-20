from random import choices


def make_array(n: int) -> list:
    """Generate the initial board of the game using random numbers

    Args:
        n (int): The size of the board

    Returns:
        array (list): The initial board (all boundary values are 0), size (n + 2) x (n + 2)
    """
    num_list = list(range(10))
    weights = [9 if i == 0 else max(0, 9 - i) for i in range(10)]
    return_array = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            return_array[i][j] = choices(num_list, weights)[0]
    return return_array

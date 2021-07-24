import random


def dumbcomputer(layout):
    """
    ai that picks spots to shoot randomly
    :param layout: hit board that tells comp whats been hit and whats missed
    :return: an i,j position where comp shoots
    """
    i = None
    j = None
    while i is None or layout[i][j] is not None:
        colength = len(layout[0])
        j = random.randint(0, colength - 1)
        rowlength = len(layout)
        i = random.randint(0, rowlength - 1)

    return i, j  # tuple


def competentcomputer(layout):
    """
    ai that picks spots to shoot specifically
    :param layout:
    :return:
    """
    pass










def alkgjw(a=1, b=1, c=5, d=10):
    print(a, b, c, d)


if __name__ == '__main__':
    alkgjw(1, 2, 3, 4)
    alkgjw(1, 2)
    alkgjw(1, 2, d=6, c=4)
    alkgjw()

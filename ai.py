import random
from operator import add


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
    hits = []
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            if layout[row][col] is True:
                hits.append((row, col))
    if len(hits) == 0:
        return dumbcomputer(layout)

    """
    go through each hit in list "hits"
    generate all adjacent positions (up down left right) for each "hit"
    each of generated positions - check if in bounds - if not, ignore - if in bounds but already fired, ignore
    if not ignored, add it to random potential firing location list
    pick random from location list (if not empty), return position. - if empty, revert back to dumb comp.
    
    """

    for hit in hits:
        up = map(add, hit, (-1,0))
        down = map(add, hit, (1,0))
        right = map(add, hit, (0,1))
        left = map(add, hit, (0,-1))









def alkgjw(a=1, b=1, c=5, d=10):
    print(a, b, c, d)


if __name__ == '__main__':
    alkgjw(1, 2, 3, 4)
    alkgjw(1, 2)
    alkgjw(1, 2, d=6, c=4)
    alkgjw()

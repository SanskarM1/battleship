from pprint import pprint
class Grid:
    def __init__(self):
        self.board_size = 10

        self.hit_board = [
            [None for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        self.ship_board = [
            [False for j in range(self.board_size)]
            for i in range(self.board_size)
        ]

        pprint(self.hit_board)
        pprint(self.ship_board)

if __name__ == '__main__':
    g = Grid()
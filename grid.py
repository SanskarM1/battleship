from pprint import pprint
from ship import Ship
import pygame


class Grid (pygame.sprite.Sprite):
    def __init__(self, computer_board):
        super().__init__()
        self.board_size = 10

        self.hit_board = [
            [None for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        self.ship_board = [
            [False for j in range(self.board_size)]
            for i in range(self.board_size)
        ]
        self.ships = []

        self.image = pygame.Surface((720-30 , 720-30) if computer_board
                                    else (20 * self.board_size, 20 * self.board_size))
        self.rect = pygame.rect.Rect((15, 15, self.image.get_width(), self.image.get_height()) if computer_board
                                     else (1280/2, 710 - self.image.get_height(),self.image.get_width(), self.image.get_height()))
        self.image.fill((255,255,255) if computer_board else (0,0,0))
        # pprint(self.hit_board)
        # pprint(self.ship_board)

    def add_ship(self, ship):
        for pos in ship.positions:
            if 0 <= pos[1] < self.board_size and 0 <= pos[0] < self.board_size and self.ship_board[pos[1]][pos[0]]:
                print("AHHHHHHHHHHHHHHHHHHHHHHHHHH")
                return False
        self.ships.append(ship)
        for pos in ship.positions:
            self.ship_board[pos[1]][pos[0]] = True
        return True


if __name__ == '__main__':
    g = Grid(True)
    g.add_ship(Ship((4, 6), "up", 3))
    g.add_ship(Ship((4, 6), "up", 3))
    print(f"length: {len(g.ships)}" )

    pprint(g.ship_board)

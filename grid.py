from pprint import pprint

import pygame

import constants
from ship import Ship


class Grid(pygame.sprite.Sprite):
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

        buffer = 15
        computer_image = (constants.SCREEN_HEIGHT - buffer * 2, constants.SCREEN_HEIGHT - buffer * 2)
        player_image = (constants.SCREEN_HEIGHT / 2 - buffer * 2, constants.SCREEN_HEIGHT / 2 - buffer * 2)
        self.image = pygame.Surface(computer_image if computer_board else player_image)

        playerX = constants.SCREEN_WIDTH / 2 + constants.SCREEN_HEIGHT / 2 - self.image.get_width() / 2

        computer_rect = (buffer, buffer, self.image.get_width(), self.image.get_height())
        player_rect = (playerX, buffer, self.image.get_width(), self.image.get_height())

        self.rect = pygame.rect.Rect(computer_rect if computer_board else player_rect)

        self.image.fill((255, 120, 255) if computer_board else (255,200,255))

        pygame.draw.line(self.image, (0,0,0) , (0,0) , (self.image.get_width(), self.image.get_height()) , 5)

    def add_ship(self, ship):
        for pos in ship.positions:
            if 0 <= pos[1] < self.board_size and 0 <= pos[0] < self.board_size and self.ship_board[pos[1]][pos[0]]:
                return False
        self.ships.append(ship)
        for pos in ship.positions:
            self.ship_board[pos[1]][pos[0]] = True
        return True


if __name__ == '__main__':
    g = Grid(True)
    g.add_ship(Ship((4, 6), "up", 3))
    g.add_ship(Ship((4, 6), "up", 3))
    print(f"length: {len(g.ships)}")

    pprint(g.ship_board)

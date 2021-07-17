from pprint import pprint

import pygame

import constants
from ship import Ship

clashofclansbomb = pygame.surface.Surface((1, 1))
explosion = pygame.surface.Surface((1, 1))
ripple = pygame.surface.Surface((1, 1))


def load_images():
    global clashofclansbomb
    global explosion
    global ripple

    clashofclansbomb = pygame.image.load("images/clashofclans-removebg-preview.png")
    clashofclansbomb.convert_alpha()
    explosion = pygame.image.load("images/explosion (1).png")
    explosion.convert_alpha()
    ripple = pygame.image.load("images/ripple (1).png")
    ripple.convert_alpha()
    temp_ripple = pygame.surface.Surface((ripple.get_width() + 44, ripple.get_height() + 44)).convert_alpha()
    temp_ripple.fill((255, 255, 255, 0))
    temp_ripple.blit(ripple, (22, 22))
    ripple = temp_ripple


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

        self.image.fill((199, 199, 199) if computer_board else (180, 180, 180))

        self.add_lines()

        self.scalebomb = pygame.transform.scale(clashofclansbomb, (
        int(self.image.get_height() / self.board_size), int(self.image.get_height() / self.board_size)))
        self.scaleripple = pygame.transform.scale(ripple, (
        int(self.image.get_height() / self.board_size), int(self.image.get_height() / self.board_size)))
        self.scaleboom = pygame.transform.scale(explosion, (
        int(self.image.get_height() / self.board_size), int(self.image.get_height() / self.board_size)))
        # self.image.blit(self.scaleboom, (0, 0))
        self.grid_image = self.image.copy()

    def add_lines(self):
        # horizontal lines
        y = 0
        for i in range(11):
            pygame.draw.line(self.image, (0, 0, 0), (0, y), (self.image.get_width(), y), 3)
            y += self.image.get_height() / self.board_size
        # vertical lines
        x = 0
        for i in range(11):
            pygame.draw.line(self.image, (0, 0, 0), (x, 0), (x, self.image.get_height()), 3)
            x += self.image.get_width() / self.board_size

        # pygame.draw.line(self.image, (0,0,0) , (0,0) , (self.image.get_width(), self.image.get_height()) , 5)

    def add_ship(self, ship):
        for pos in ship.positions:
            if 0 <= pos[1] < self.board_size and 0 <= pos[0] < self.board_size and self.ship_board[pos[1]][pos[0]]:
                return False
        self.ships.append(ship)
        for pos in ship.positions:
            self.ship_board[pos[1]][pos[0]] = True
        return True

    def shoot_at(self, position):
        """
        marks where player shoots
        :param position: position of attack - tuple [int, int]
        :return: true if hit / false otherwise BOOLEAN :)
        """
        x, y = position
        if self.hit_board[y][x] is not None:
            return None
        if not self.ship_board[y][x]:
            self.hit_board[y][x] = False
            return False
        self.hit_board[y][x] = True
        return True

    def draw_on(self, surf):
        pass

    def handle_event(self, ev):

        if ev.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            colu = (x - 15) // (self.image.get_width() / self.board_size)
            ro = (y - 15) // (self.image.get_width() / self.board_size)
            self.image = self.grid_image.copy()
            self.image.blit(self.scalebomb, (
                colu * self.image.get_width() / self.board_size, ro * self.image.get_width() / self.board_size))

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            colu = (x - 15) // (self.image.get_width() / self.board_size)
            ro = (y - 15) // (self.image.get_width() / self.board_size)
            didhit = self.shoot_at((int(colu), int(ro)))
            if didhit is not None:
                self.grid_image.blit(self.scaleboom if didhit else self.scaleripple, (
                colu * self.image.get_width() / self.board_size, ro * self.image.get_width() / self.board_size))



if __name__ == '__main__':
    g = Grid(True)
    g.add_ship(Ship((4, 6), "up", 3))
    g.add_ship(Ship((4, 6), "up", 3))
    print(f"length: {len(g.ships)}")

    pprint(g.ship_board)

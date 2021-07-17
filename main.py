from datetime import datetime

import pygame

import constants
import grid
from grid import Grid
from ship import Ship

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("GTA 6")
clock = pygame.time.Clock()
isGameRunning = True
grid.load_images()
player_grid = Grid(False)
computer_grid = Grid(True)
computer_grid.add_ship(Ship((4, 6), "up", 3))
grid_group = pygame.sprite.Group(player_grid, computer_grid)
current_time = datetime.now()
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        computer_grid.handle_event(event)
    screen.fill((100, 0, 255))
    pygame.draw.circle(screen, (0, 0, 0), (600, 600), 20)
    grid_group.draw(screen)
    time_elapsed = datetime.now() - current_time
    font = pygame.font.SysFont("Arial", 12, True)
    render_text = font.render(str(int(1 / time_elapsed.total_seconds())), True, (0, 0, 0))
    screen.blit(render_text, (constants.SCREEN_WIDTH - render_text.get_width(), 0))

    pygame.display.flip()

    current_time = datetime.now()

    clock.tick(60)

pygame.quit()

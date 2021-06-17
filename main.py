import pygame
from grid import Grid
import constants
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("GTA 6")
clock = pygame.time.Clock()
isGameRunning = True
player_grid = Grid(False)
computer_grid = Grid(True)
grid_group = pygame.sprite.Group(player_grid, computer_grid)
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
    screen.fill((100,0,255))
    pygame.draw.circle(screen,(0,0,0),(600,600),20)
    grid_group.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()





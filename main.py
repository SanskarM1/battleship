import pygame

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GTA 6")
clock = pygame.time.Clock()
isGameRunning = True
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
    screen.fill((100,0,255))
    pygame.draw.circle(screen,(0,0,0),(600,600),20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()





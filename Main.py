import pygame
from PlayerController import Player
from GlobalVariables import *

pygame.init()

# game window initialization
timer = pygame.time.Clock()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Knight")

background = pygame.image.load('background.jpg')

player = Player(300, 300, 64, 64)


def redrawWindow():
    window.blit(background, (0, 0))
    player.redraw(window)
    pygame.display.update()


# MAIN GAME LOOP
running = True
while running:
    timer.tick(player.sprites * frameSpeed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.movement()
    redrawWindow()

pygame.quit()

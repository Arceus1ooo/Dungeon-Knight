import pygame
from PlayerController import Player

pygame.init()

# GLOBAL VARIABLES (these declarations should be in every script)
screenWidth = 500
screenHeight = 480
frameSpeed = 9

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

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.speed:
        player.x -= player.speed
        player.left = True
        player.right = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.speed:
        player.x += player.speed
        player.left = False
        player.right = True
    else:
        player.left = False
        player.right = False
        steps = 0
    if keys[pygame.K_UP] and player.y > player.speed:
        player.y -= player.speed
    if keys[pygame.K_DOWN] and player.y < screenHeight - player.height - player.speed:
        player.y += player.speed
    redrawWindow()

pygame.quit()

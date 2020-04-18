import pygame
from GlobalVariables import *
from PlayerController import Player
from Triggers import RoomSwitch

pygame.init()

# game window initialization
timer = pygame.time.Clock()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Knight")

player = Player(300, 300, 64, 64)
rightSwitch = RoomSwitch(screenWidth - 5, screenHeight / 2, 5, 40, 'right')


def redrawWindow():
    background = pygame.image.load(map[mapX][mapY])
    window.blit(background, (0, 0))
    player.redraw(window)
    rightSwitch.redraw(window)
    pygame.display.update()  # This should always be last


def detectCollision(obj1, obj2):
    if (obj1.x + obj1.width) > obj2.x and obj1.x < (obj2.x + obj2.width):
        if (obj1.y + obj1.height) > obj2.y and obj1.y < (obj2.y + obj2.height):
            return True
    else:
        return False


# MAIN GAME LOOP
running = True
while running:
    timer.tick(player.sprites * frameSpeed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    collision = detectCollision(player, rightSwitch)
    if collision and mapY < mapYMax:
        mapY = rightSwitch.trigger(mapX, mapY)
        player.x = 0
    player.movement()
    # print("Map X: " + str(mapX) + ", Map Y: " + str(mapY))
    redrawWindow()

pygame.quit()

import pygame
from GlobalVariables import *
from PlayerController import Player
from Triggers import RoomSwitch

pygame.init()

# game window initialization
timer = pygame.time.Clock()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Knight")

# object instantiation
player = Player(300, 300, 64, 64)
rightSwitch = RoomSwitch(screenWidth - 5, screenHeight / 2, 5, 40, 'right', mainRoom)
topSwitch = RoomSwitch(screenWidth / 2, 0, 40, 5, 'up', mainRoom)
leftSwitch = RoomSwitch(0, screenHeight / 2, 5, 40, 'left', mainRoom)
bottomSwitch = RoomSwitch(screenWidth / 2, screenHeight - 5, 40, 5, 'down', mainRoom)
roomSwitches = [leftSwitch, rightSwitch, topSwitch, bottomSwitch]


def render(objects=None):
    if objects is None:
        objects = []
    for obj in objects:
        if obj.x > 0 and obj.y > 0:
            obj.visible = True
        else:
            obj.visible = False


def redrawWindow():
    room = map[mapX][mapY]
    window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
    player.redraw(window)
    for switch in roomSwitches:
        switch.redraw(window, room)
    pygame.display.update()  # This should always be last


# MAIN GAME LOOP
running = True
while running:
    timer.tick(player.sprites * frameSpeed)
    render(roomSwitches)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.cooldown == 0:
                player.cooldown = 1
                player.attacking = True

    # Player collisions with room switches
    for switch in roomSwitches:
        switch.collision = switch.detectCollision(player)
        if switch.collision:
            if switch.direction == 'right' or switch.direction == 'left':
                mapY = switch.trigger(mapY)
                player.x = switch.postTrigger(player.width, player.height)
            elif switch.direction == 'up' or switch.direction == 'down':
                mapX = switch.trigger(mapX)
                player.y = switch.postTrigger(player.width, player.height)
            print("Map X: " + str(mapX) + ", Map Y: " + str(mapY))

    player.movement()
    redrawWindow()

pygame.quit()

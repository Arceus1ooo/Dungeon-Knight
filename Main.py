import pygame
from GlobalVariables import *
from PlayerController import Player
from Triggers import RoomSwitch
from EnemyController import Enemy
from Obstacles import LWall
from ObjectMover import moveObj

pygame.init()

# game window initialization
timer = pygame.time.Clock()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Knight")

# object instantiation
player = Player(300, 300, 64, 64)

rightSwitch = RoomSwitch(screenWidth - 6, (screenHeight / 2) - 90, 5, 138, 'right', [mainRoom, room4, room2])
topSwitch = RoomSwitch((screenWidth / 2) - 115, 1, 226, 5, 'up', [mainRoom, room7, room6, room4, room8])
leftSwitch = RoomSwitch(1, (screenHeight / 2) - 90, 5, 145, 'left', [mainRoom, room5, room3])
bottomSwitch = RoomSwitch((screenWidth / 2) - 115, screenHeight - 6, 226, 5, 'down',
                          [mainRoom, room2, room4, room1, room3, room5])
roomSwitches = [leftSwitch, rightSwitch, topSwitch, bottomSwitch]

yeti = Enemy(20, 200, 64, 64, 'spr_ape_yeti.png')
enemy_list = pygame.sprite.Group()
enemy_list.add(yeti)
enemies = [yeti]

topLeft = LWall(0, 0, 365, 250, 0.27, 0.39, allRooms, 'topLeft')
topRight = LWall(screenWidth, 0, 365, 250, 0.27, 0.38, allRooms, 'topRight')
bottomLeft = LWall(0, screenHeight, 365, 295, 0.27, 0.2, allRooms, 'bottomLeft')
bottomRight = LWall(screenWidth, screenHeight, 365, 295, 0.25, 0.2, allRooms, 'bottomRight')
walls = [topLeft, topRight, bottomLeft, bottomRight]

block1 = moveObj(400, 400, 25, 25, [mainRoom])
movingBlocks = [block1]


def redrawWindow():
    room = map[mapX][mapY]
    window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
    player.redraw(window)
    enemy_list.draw(window)
    for e in enemy_list:
        e.moveTowardsPlayer(player)
    for e in enemies:
        if e.health == 0:
            e.rect.x = -1000
            e.rect.y = -1000
            e.speed = 0
    for switch in roomSwitches:
        switch.redraw(window, room)
    for block in movingBlocks:
        block.redraw(window, room)
    for wall in walls:
        wall.redraw(window)
    pygame.display.update()  # This should always be last


# MAIN GAME LOOP
running = True
while running:
    timer.tick(player.sprites * frameSpeed)
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

    for block in movingBlocks:
        block.checkCollision(player)
    
    for wall in walls:
        wall.detectCollision(player)
    player.movement()
    redrawWindow()

pygame.quit()

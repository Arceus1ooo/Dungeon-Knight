import pygame
from GlobalVariables import *
from PlayerController import Player, Javelin
from Triggers import RoomSwitch
from EnemyController import Enemy
from Obstacles import LWall, Barricade
from ObjectMover import moveObj
from Puzzle import puzzle

pygame.init()

# game window initialization
timer = pygame.time.Clock()
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dungeon Knight")
pygame.mouse.set_visible(False)
pointerImg = pygame.image.load('pointer.png')
pointerImg = pygame.transform.scale(pointerImg, (50, 50))
pointerRect = pointerImg.get_rect()

# object instantiation
player = Player(300, 300, 64, 64)
javelins = []

rightSwitch = RoomSwitch(screenWidth - 5, (screenHeight / 2) - 75, 5, 100, 'right', [mainRoom, room2, room4])
leftSwitch = RoomSwitch(0, (screenHeight / 2) - 75, 5, 100, 'left', [mainRoom, room3, room5])
bottomSwitch = RoomSwitch(screenWidth / 2 - 75, screenHeight - 5, 150, 5, 'down',
                          [mainRoom, room1, room2, room4, room5])
topSwitch = RoomSwitch(screenWidth / 2 - 75, 0, 150, 5, 'up', [mainRoom, room7, room6, room4, room8])
roomSwitches = [rightSwitch, leftSwitch, topSwitch, bottomSwitch]

yeti = Enemy(100, 300, 64, 64, 'spr_ape_yeti.png')
enemy_list = pygame.sprite.Group()
enemies = [yeti]

topLeft = LWall(0, 0, 365, 250, 0.27, 0.39, 'topLeft')
topRight = LWall(screenWidth, 0, 365, 250, 0.27, 0.38, 'topRight')
bottomLeft = LWall(0, screenHeight, 365, 295, 0.27, 0.2, 'bottomLeft')
bottomRight = LWall(screenWidth, screenHeight, 365, 295, 0.25, 0.2, 'bottomRight')
leftWall = Barricade(0, topLeft.y + topLeft.height, topLeft.scaledWidth, topLeft.scaledHeight + 40, gray,
                     [room6, room4, room1, room7, room2, room8])
topWall = Barricade(topLeft.x + topLeft.width, 0, topLeft.scaledWidth + 135, topLeft.scaledHeight, gray,
                    [room1, room2, room3, room5])
rightWall = Barricade(screenWidth - bottomRight.scaledWidth, topRight.y + topRight.height, topRight.scaledWidth,
                      topRight.scaledHeight + 40, gray, [room6, room1, room7, room8, room5, room3])
bottomWall = Barricade(topLeft.x + topLeft.width, screenHeight - bottomRight.scaledHeight,
                       bottomLeft.scaledWidth + 135, topLeft.scaledHeight, gray, [room6, room7, room8, room3])
barrier11 = Barricade(300, 400, 325, 10, black, [room5])
barrier12 = Barricade(335, 410, 10, 215, black, [room5])
walls = [topLeft, topRight, bottomLeft, bottomRight, leftWall, topWall, rightWall, bottomWall, barrier11, barrier12]

block11 = moveObj(150, 250, 25, 25, [room5])
block12 = moveObj(200, 250, 25, 25, [room5])
block13 = moveObj(550, 100, 25, 25, [room5])
block2 = moveObj(300, 400, 25, 25, [room1])
block3 = moveObj(300, 400, 25, 25, [room2])
block4 = moveObj(300, 400, 25, 25, [room3])
block5 = moveObj(300, 400, 25, 25, [room4])
block6 = moveObj(300, 400, 25, 25, [room6])
movingBlocks = [block11, block12, block13, block2, block3, block4, block5, block6]

puzzle11 = puzzle(300, 100, 10, 300, 100, 200, [room5])
puzzle12 = puzzle(600, 100, 10, 300, 300, 500, [room5])
puzzle13 = puzzle(100, 400, 200, 10, 550, 300, [room5])
puzzle14 = puzzle(390, 645, 200, 10, 325, 100, [room5])
puzzle2 = puzzle(400, 150, 10, 70, 100, 200, [room1])
puzzle3 = puzzle(400, 150, 10, 70, 100, 200, [room2])
puzzle4 = puzzle(400, 150, 10, 70, 100, 200, [room3])
puzzle5 = puzzle(400, 150, 10, 70, 100, 200, [room4])
puzzle6 = puzzle(400, 150, 10, 70, 100, 200, [room6])
puzzles = [puzzle11, puzzle12, puzzle13, puzzle14, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6]



def redrawWindow():
    room = map[mapX][mapY]
    window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
    window.blit(pointerImg, pointerRect)
    player.redraw(window)
    enemy_list.draw(window)
    if mapX == 1 and mapY == 1:
        enemy_list.add(yeti)
        enemy_list.draw(window)
    else:
        enemy_list.remove(yeti)
    for e in enemy_list:
        e.moveTowardsPlayer(player)
    for e in enemies:
        if e.health == 0:
            enemy_list.remove(e)
            e.kill()
            window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
            player.redraw(window)
    for javelin in javelins:
        javelin.redraw(window)
    for switch in roomSwitches:
        switch.redraw(window, room)
    for puzzle in puzzles:
        puzzle.redraw(window, room)
    for block in movingBlocks:
        block.redraw(window, room)
    for wall in walls:
        wall.redraw(window, room)
    pygame.display.update()  # This should always be last


# MAIN GAME LOOP
running = True
while running:
    timer.tick(player.sprites * frameSpeed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and len(javelins) == 0:
            javelins.append(
                Javelin(player.x + player.width / 2, player.y + player.height / 2, pygame.mouse.get_pos()))
    mouse = pygame.mouse.get_pos()
    pointerRect.topleft = (mouse[0] - 5, mouse[1] - 5)
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
            
    for javelin in javelins:
        for e in enemy_list:
            if (javelin.rect.x + javelin.width) > e.rect.x and javelin.rect.x < (e.rect.x + e.width):
                if (javelin.rect.y + javelin.height) > e.rect.y and javelin.rect.y < (e.rect.y + e.height):
                    e.health -= player.attack
                    print(e.health)
    for e in enemy_list:
            if (e.rect.x + e.width) > player.x and e.rect.x < (player.x + player.width):
                if (e.rect.y + e.height) > player.y and e.rect.y < (player.y + player.height):
                    player.health -= e.attack
                    print(player.health)
        

    for block in movingBlocks:
        block.checkCollision(player)
    for w in puzzles:
        w.wallCollision(player)
        for block in movingBlocks:
            w.wallCollision(block)
    for p in puzzles:
        p.buttonPress(player)
        for block in movingBlocks:
            if p.buttonPress(block):
                break  
    for wall in walls:
        wall.detectCollision(player)
        for block in movingBlocks:
            wall.detectCollision(block)
    for javelin in javelins:
        if javelin.visible is False:
            javelins.pop()
    player.movement()
    redrawWindow()

pygame.quit()

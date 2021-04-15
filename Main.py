import pygame
from GlobalVariables import screenWidth, screenHeight, frameSpeed, mainRoom, room1, room2
from GlobalVariables import room3, room4, room5, room6, room7, room8, gray, black, mapX, mapY
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

rightSwitch = RoomSwitch(screenWidth - 5, (screenHeight / 2) - 75, 5, 100,
                         'right', [mainRoom, room2, room4])
leftSwitch = RoomSwitch(0, (screenHeight / 2) - 75, 5, 100, 'left',
                        [mainRoom, room3, room5])
bottomSwitch = RoomSwitch(screenWidth / 2 - 75, screenHeight - 5, 150, 5,
                          'down', [mainRoom, room1, room2, room4, room5])
topSwitch = RoomSwitch(screenWidth / 2 - 75, 0, 150, 5, 'up',
                       [mainRoom, room7, room6, room4, room8])
roomSwitches = [rightSwitch, leftSwitch, topSwitch, bottomSwitch]

yeti = Enemy(100, 300, 64, 64, 'spr_ape_yeti.png')
enemy_list = pygame.sprite.Group()
enemies = [yeti]

topLeft = LWall(0, 0, 365, 250, 0.27, 0.39, 'topLeft')
topRight = LWall(screenWidth, 0, 365, 250, 0.27, 0.38, 'topRight')
bottomLeft = LWall(0, screenHeight, 365, 295, 0.27, 0.2, 'bottomLeft')
bottomRight = LWall(screenWidth, screenHeight, 365, 295, 0.25, 0.2,
                    'bottomRight')

leftWall = Barricade(0, topLeft.y + topLeft.height, topLeft.scaledWidth,
                     topLeft.scaledHeight + 40, gray,
                     [room6, room4, room1, room7, room2, room8])

topWall = Barricade(topLeft.x + topLeft.width, 0, topLeft.scaledWidth + 135,
                    topLeft.scaledHeight, gray, [room1, room2, room3, room5])

rightWall = Barricade(screenWidth - bottomRight.scaledWidth,
                      topRight.y + topRight.height, topRight.scaledWidth,
                      topRight.scaledHeight + 40, gray,
                      [room6, room1, room7, room8, room5, room3])

bottomWall = Barricade(topLeft.x + topLeft.width,
                       screenHeight - bottomRight.scaledHeight,
                       bottomLeft.scaledWidth + 135, topLeft.scaledHeight,
                       gray, [room6, room7, room8, room3])

barrier11 = Barricade(300, 400, 325, 10, black, [room5])
barrier12 = Barricade(335, 410, 10, 215, black, [room5])
walls = [topLeft, topRight, bottomLeft, bottomRight, leftWall, topWall,
         rightWall, bottomWall, barrier11, barrier12]
barriers = [leftWall, topWall, rightWall, bottomWall, barrier11, barrier12]

block51 = moveObj(150, 250, 25, 25, [room5])
block52 = moveObj(200, 250, 25, 25, [room5])
block53 = moveObj(550, 100, 25, 25, [room5])
block2 = moveObj(300, 400, 25, 25, [room2])
block4 = moveObj(400, 400, 25, 25, [room4])
movingBlocks = [block51, block52, block53, block2, block4]

puzzle51 = puzzle(300, 100, 10, 300, 100, 200, [room5])
puzzle52 = puzzle(600, 100, 10, 300, 300, 500, [room5])
puzzle53 = puzzle(100, 400, 200, 10, 550, 300, [room5])
puzzle54 = puzzle(390, 645, 200, 10, 325, 100, [room5])

puzzle41 = puzzle(390, 100, 200, 10, 100, 500, [room4])
puzzle42 = puzzle(390, 625, 200, 10, 100, 200, [room4])

puzzle2 = puzzle(880, 250, 10, 130, 100, 200, [room2])

puzzles = [puzzle51, puzzle52, puzzle53, puzzle54, puzzle41, puzzle42, puzzle2]


def redrawWindow():
    room = map[mapX][mapY]
    for enemy in enemies:
        if enemy.health > 0:
            window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
    enemy_list.draw(window)
    if mapX == 1 and mapY == 1:
        enemy_list.add(yeti)
        enemy_list.draw(window)
    else:
        enemy_list.remove(yeti)
    for enemy in enemies:
        enemy.moveTowardsPlayer(player)
        if enemy.health == 0:
            enemy.kill()
            window.blit(pygame.image.load(map[mapX][mapY]), (0, 0))
            player.redraw(window)
    for javelin in javelins:
        javelin.redraw(window)
    for switch in roomSwitches:
        switch.redraw(window, room)
    for item in puzzles:
        item.redraw(window, room)
    for block in movingBlocks:
        block.redraw(window, room)
    for wall in walls:
        wall.redraw(window, room)
    window.blit(pointerImg, pointerRect)
    player.redraw(window)
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
                Javelin(player.x + player.width / 2,
                        player.y + player.height / 2, pygame.mouse.get_pos()))
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
        for enemy in enemy_list:
            if javelin.detectCollision(enemy):
                enemy.health -= player.attack
                javelin.visible = False
                # print(e.health)
        for w in walls:
            if w.detectRectCollision(javelin):
                javelin.visible = False

    for enemy in enemy_list:
        if((enemy.rect.x + enemy.width) > player.x and enemy.rect.x < (player.x + player.width)):
            if ((enemy.rect.y + enemy.height) > player.yeti and enemy.rect.y < (player.y + player.height)):
                player.health -= enemy.attack
                # print(player.health)

    for block in movingBlocks:
        block.checkCollision(player)
    for w in puzzles:
        w.wallCollision(player)
        for block in movingBlocks:
            block.collisionBlock(w)
    for bar in barriers:
        for block in movingBlocks:
            block.collisionBlock(bar)

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

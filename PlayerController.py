import pygame
from GlobalVariables import *

# player sprites
character = pygame.image.load('player/standing.png')
walkRight = [pygame.image.load('player/R1.png'), pygame.image.load('player/R2.png'), pygame.image.load('player/R3.png'),
             pygame.image.load('player/R4.png'), pygame.image.load('player/R5.png'), pygame.image.load('player/R6.png'),
             pygame.image.load('player/R7.png'), pygame.image.load('player/R8.png'), pygame.image.load('player/R9.png')]
walkLeft = [pygame.image.load('player/L1.png'), pygame.image.load('player/L2.png'), pygame.image.load('player/L3.png'),
            pygame.image.load('player/L4.png'), pygame.image.load('player/L5.png'), pygame.image.load('player/L6.png'),
            pygame.image.load('player/L7.png'), pygame.image.load('player/L8.png'), pygame.image.load('player/L9.png')]


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2
        self.direction = 'down'
        self.steps = 0
        self.sprites = len(walkRight)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.cooldown = 0
        self.cooldownMax = 60
        self.attacking = False
        self.switch = True
        self.rightSword = Sword(self.x + self.width, self.y + self.height / 2, swordWidth, swordHeight)
        self.leftSword = Sword(self.x - swordWidth, self.y + self.height / 2, swordWidth, swordHeight)
        self.upSword = Sword(self.x + self.width / 2, self.y - swordWidth, swordHeight, swordWidth)
        self.downSword = Sword(self.x + self.width / 2, self.y + self.height, swordHeight, swordWidth)
        self.swords = [self.rightSword, self.leftSword, self.upSword, self.downSword]
        self.temp = (self.direction,)
        self.health = 5
        self.attack = 1

    def redraw(self, win):  # player animation, called once per frame
        if self.cooldown > 0:
            self.cooldown += 1
        if self.cooldown > self.cooldownMax:
            self.cooldown = 0
            self.attacking = False

        self.swordDisplay(win)
        if self.attacking:
            self.speed = 0
        else:
            self.speed = 2
            self.switch = True

        if self.steps + 1 > len(walkRight) * frameSpeed:
            self.steps = 0
        if self.direction == 'left' and not self.attacking:
            win.blit(walkLeft[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        elif self.direction == 'right' and not self.attacking:
            win.blit(walkRight[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        else:
            if self.direction == 'right':
                win.blit(walkRight[0], (self.x, self.y))
            elif self.direction == 'left':
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(character, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, self.hitbox, 1)

    def swordDisplay(self, win):
        if self.switch:
            self.temp = (self.direction,)
            self.switch = False

        if self.cooldown <= self.cooldownMax / 2:  # extend sword
            if self.temp[0] == 'right' and self.attacking:
                self.rightSword = Sword(self.x + self.width, self.y + self.height / 2,
                                        swordWidth + self.cooldown, swordHeight)
                self.rightSword.redraw(win)
            elif self.temp[0] == 'left' and self.attacking:
                self.leftSword = Sword(self.x - self.cooldown - 5, self.y + self.height / 2,
                                       swordWidth + self.cooldown, swordHeight)
                self.leftSword.redraw(win)
            elif self.temp[0] == 'up' and self.attacking:
                self.upSword = Sword(self.x + self.width / 2, self.y - self.cooldown - 5,
                                     swordHeight, swordWidth + self.cooldown)
                self.upSword.redraw(win)
            elif self.temp[0] == 'down' and self.attacking:
                self.downSword = Sword(self.x + self.width / 2, self.y + self.height,
                                       swordHeight, swordWidth + self.cooldown)
                self.downSword.redraw(win)
        else:  # retract sword
            if self.temp[0] == 'right' and self.attacking:
                self.rightSword = Sword(self.x + self.width, self.y + self.height / 2,
                                        swordWidth + (self.cooldownMax - self.cooldown), swordHeight)
                self.rightSword.redraw(win)
            elif self.temp[0] == 'left' and self.attacking:
                self.leftSword = Sword(self.x - (self.cooldownMax - self.cooldown) - 5, self.y + self.height / 2,
                                       swordWidth + (self.cooldownMax - self.cooldown), swordHeight)
                self.leftSword.redraw(win)
            elif self.temp[0] == 'up' and self.attacking:
                self.upSword = Sword(self.x + self.width / 2, self.y - (self.cooldownMax - self.cooldown) - 5,
                                     swordHeight, swordWidth + (self.cooldownMax - self.cooldown))
                self.upSword.redraw(win)
            elif self.temp[0] == 'down' and self.attacking:
                self.downSword = Sword(self.x + self.width / 2, self.y + self.height,
                                       swordHeight, swordWidth + (self.cooldownMax - self.cooldown))
                self.downSword.redraw(win)

        if self.attacking is False:
            for sword in self.swords:
                sword.redraw(win, False)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.speed:
            self.x -= self.speed
            self.direction = 'left'
        elif keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.speed:
            self.x += self.speed
            self.direction = 'right'
        else:
            self.steps = 0
        if keys[pygame.K_UP] and self.y > self.speed:
            self.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_DOWN] and self.y < screenHeight - self.height - self.speed:
            self.y += self.speed
            self.direction = 'down'

    def reset(self):
        self.x = screenWidth / 2
        self.y = screenHeight / 2


class Sword:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = (self.x, self.y)

    def redraw(self, win, visible=True):
        if visible:
            self.x = self.position[0]
            self.y = self.position[1]
            pygame.draw.rect(win, black, (self.x, self.y, self.width, self.height))
        else:
            self.x = -1000
            self.y = -1000

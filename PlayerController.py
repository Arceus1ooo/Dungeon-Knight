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
        self.left = False
        self.right = False
        self.steps = 0
        self.sprites = len(walkRight)
        self.hitbox = (self.x, self.y, self.width, self.height)

    def redraw(self, win):  # player animation
        if self.steps + 1 > len(walkRight) * frameSpeed:
            self.steps = 0
        if self.left:
            win.blit(walkLeft[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        elif self.right:
            win.blit(walkRight[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(character, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, self.hitbox, 1)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.speed:
            self.x -= self.speed
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.speed:
            self.x += self.speed
            self.left = False
            self.right = True
        else:
            self.steps = 0
        if keys[pygame.K_UP] and self.y > self.speed:
            self.y -= self.speed
            self.left = False
            self.right = False
        if keys[pygame.K_DOWN] and self.y < screenHeight - self.height - self.speed:
            self.y += self.speed
            self.left = False
            self.right = False

    def reset(self):
        self.x = screenWidth / 2
        self.y = screenHeight / 2

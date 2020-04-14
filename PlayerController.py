import pygame

# GLOBAL VARIABLES (these declaration should be in every script)
screenWidth = 500
screenHeight = 480
frameSpeed = 9

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
            win.blit(character, (self.x, self.y))

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
            self.left = False
            self.right = False
            steps = 0
        if keys[pygame.K_UP] and self.y > self.speed:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < screenHeight - self.height - self.speed:
            self.y += self.speed

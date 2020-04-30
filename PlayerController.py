import pygame
from GlobalVariables import *
import math

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
        self.attacking = False
        self.temp = (self.direction,)
        self.health = 5
        self.attack = 1
        self.animate = False
        self.alpha = 255

    def redraw(self, win):  # player animation, called once per frame
        if self.attacking:
            self.speed = 0
        else:
            self.speed = 2

        if self.steps + 1 > len(walkRight) * frameSpeed:
            self.steps = 0
        if self.direction == 'left' and not self.attacking and self.animate:
            win.blit(walkLeft[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        elif self.direction == 'right' and not self.attacking and self.animate:
            win.blit(walkRight[int(self.steps / frameSpeed)], (self.x, self.y))
            self.steps += 1
        else:
            if self.direction == 'right':
                win.blit(walkRight[0], (self.x, self.y))
            elif self.direction == 'left':
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(character, (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 16, 28, 50)
        pygame.draw.rect(win, red, self.hitbox, 1)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.speed:
            self.animate = True
            self.x -= self.speed
            self.direction = 'left'
        elif keys[pygame.K_RIGHT] and self.x < screenWidth - self.width - self.speed:
            self.animate = True
            self.x += self.speed
            self.direction = 'right'
        elif keys[pygame.K_UP] and self.y > self.speed:
            self.y -= self.speed
            self.direction = 'up'
        elif keys[pygame.K_DOWN] and self.y < screenHeight - self.height - self.speed:
            self.y += self.speed
            self.direction = 'down'
        else:
            self.animate = False
        if self.direction == 'up' or self.direction == 'down':
            self.steps = 0

    def reset(self):
        self.x = screenWidth / 2
        self.y = screenHeight / 2


class Javelin:
    def __init__(self, x, y, mousePos):
        self.speed = 8
        self.image = pygame.image.load('javelin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 5
        self.height = 2
        self.position = (self.rect.x, self.rect.y)
        self.mousePos = mousePos
        self.visible = True
        self.direction = pygame.math.Vector2(self.mousePos[0] - self.rect.x, self.mousePos[1] - self.rect.y)
        self.angle = (180 / math.pi) * math.atan2(self.direction.x, self.direction.y) + 180
        self.image = pygame.transform.rotate(self.image, int(self.angle))
        self.rect = self.image.get_rect(center=self.position)

    def redraw(self, win):
        self.direction = pygame.math.Vector2(self.mousePos[0] - self.rect.x, self.mousePos[1] - self.rect.y)
        if self.direction.x <= 2 and self.direction.y <= 2:
            self.visible = False
        else:
            self.direction.normalize()
            self.direction.scale_to_length(self.speed)
            self.rect.move_ip(self.direction)
            win.blit(self.image, (self.rect.x, self.rect.y))

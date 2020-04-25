import pygame
import sys
import os
import math
import time
from pygame.locals import *

ALPHA = (0, 255, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('enemies', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.counter = 0
        self.speed = 2
        self.health = 2
        self.attack = 1
    def moveTowardsPlayer(self, player):
        dirvect = pygame.math.Vector2(player.x - self.rect.x, player.y - self.rect.y)
        if dirvect == (0,0):
            player.health -= self.attack
            self.speed = 0
        else:
            self.speed = 2
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)

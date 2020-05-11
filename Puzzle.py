import pygame
from GlobalVariables import *
import random

not_press = 1

class puzzle:
    def __init__(self, x, y, width, height, x_button, y_button, rooms):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rooms = rooms
        self.existence = 0
        self.position = (self.x, self.y)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.alpha = 255
        self.x_button = x_button
        self.y_button = y_button
        self.not_press = 1

    def wallCollision(self, sprite):
        if (self.x + self.width) > sprite.x and self.x < (sprite.x + sprite.width):
            if (self.y + self.height) > sprite.y and self.y < (sprite.y + sprite.height):
                if self.existence > 0 and self.not_press == 1:
                    if sprite.direction == 'up':
                        sprite.y += sprite.speed
                    elif sprite.direction == 'down':
                        sprite.y -= sprite.speed
                    elif sprite.direction == 'left':
                        sprite.x += sprite.speed
                    else:
                        sprite.x -= sprite.speed
                    return True
        else:
            return False

    def redraw(self, win, roomNum):
        self.existence = 0
        for room in self.rooms:
            if room == roomNum:
                self.existence += 1
        if self.existence > 0 and self.not_press == 1:
            self.alpha = 255
            b = pygame.Surface((30, 30))
            b.set_alpha(self.alpha)
            b.fill(self.color)
            win.blit(b, (self.x_button, self.y_button))
            s = pygame.Surface((self.width, self.height))
            s.set_alpha(self.alpha)
            s.fill(self.color)
            win.blit(s, (self.x, self.y))
        else:
            self.alpha = 0
            s = pygame.Surface((self.width, self.height))
            s.set_alpha(self.alpha)
            s.fill(self.color)
            win.blit(s, (self.x, self.y))
            b = pygame.Surface((30, 30))
            b.set_alpha(self.alpha)
            b.fill(self.color)
            win.blit(b, (self.x_button, self.y_button))

    def buttonPress(self, sprite):
        if sprite.existence > 0:
            if (self.x_button + 30) > sprite.x and self.x_button < (sprite.x + sprite.width):
                if (self.y_button + 30) > sprite.y and self.y_button < (sprite.y + sprite.height):
                    if self.existence > 0:
                        self.not_press = 0
                        return True
            else:
                self.not_press = 1
                return False


   



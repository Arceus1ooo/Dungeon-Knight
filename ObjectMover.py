import pygame
from GlobalVariables import *
from PlayerController import Player
from Obstacles import LWall


class moveObj:
    def __init__(self, x, y, width, height, rooms):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = ""
        self.rooms = rooms
        self.position = (self.x, self.y)
        self.existence = 0
        self.speed = 2
        self.color = brown

    def redraw(self, win, mapRoom):
        self.existence = 0
        for room in self.rooms:
            if room == mapRoom:
                self.existence += 1
        if self.existence > 0:
            self.x = self.position[0]
            self.y = self.position[1]
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        else:
            self.x = -1000
            self.y = -1000

    def checkCollision(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                if self.existence > 0:
                    if obj.direction == 'right' and self.x < screenWidth - 120:
                        self.direction = "right"
                        self.x += self.speed
                    elif obj.direction == 'left' and self.x > 100:
                        self.direction = "left"
                        self.x -= self.speed
                    elif obj.direction == 'up' and self.y > 100:
                        self.direction = "up"
                        self.y -= self.speed
                    elif obj.direction == 'down' and self.y < screenHeight - 85:
                        self.direction = "down"
                        self.y += self.speed
                    self.position = (self.x, self.y)
                    return True
        else:
            return False

    def collisionBlock(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                if self.existence > 0 and obj.alpha == 255:
                    if self.direction == 'right' and self.x < screenWidth - 100:
                        self.x -= self.speed
                    elif self.direction == 'left' and self.x > 100:
                        self.x += self.speed
                    elif self.direction == 'up' and self.y > 100:
                        self.y += self.speed
                    elif self.direction == 'down' and self.y < screenHeight - 85:
                        self.y -= self.speed
                    self.position = (self.x, self.y)
                    return True
        else:
            return False


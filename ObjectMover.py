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
        self.collision = False
        self.rooms = rooms
        self.position = [self.x, self.y]
        self.existence = 0

    def redraw(self, win, roomNum):
        self.existence = 0
        for room in self.rooms:
            if room == roomNum:
                self.existence += 1
        if self.existence > 0:
            s = pygame.Surface((25, 25))
            s.set_alpha(255)
            s.fill(red)
            win.blit(s, (self.x, self.y))
        else:
            s = pygame.Surface((25, 25))
            s.set_alpha(0)
            s.fill(red)
            win.blit(s, (self.x, self.y))

    def checkCollision(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                if obj.direction == 'right' and self.x < screenWidth - self.width:
                    self.x += obj.speed
                elif obj.direction == 'left' and self.x > 0:
                    self.x -= obj.speed
                elif obj.direction == 'up' and self.y > 0:
                    self.y -= obj.speed
                elif obj.direction == 'down' and self.y < screenHeight - self.height:
                    self.y += obj.speed
                return True
        else:
            return False

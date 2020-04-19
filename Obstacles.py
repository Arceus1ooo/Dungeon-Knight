import pygame
from GlobalVariables import *


class Obstacle:
    def __init__(self, x, y, width, height, room):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room = room
        self.position = (self.x, self.y)
        self.visible = True

    def detectCollision(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                return True
        else:
            return False

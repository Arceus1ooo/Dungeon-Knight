import pygame
from GlobalVariables import *
from PlayerController import Player



class moveObj:
    def __init__(self, x, y, width, height, rooms):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision = False
        self.rooms = rooms
        self.position = (self.x, self.y)
        self.existence = 0

    def redraw(self, win):
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height), 1)

    def checkCollision(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                if obj.direction == 'right' and self.x < screenWidth:
                    self.x += 5
                elif obj.direction == 'left' and self.x > 0:
                    self.x -= 5
                elif obj.direction == 'up' and self.y > 0:
                    self.y -= 5
                elif obj.direction == 'down' and self.y < screenHeight:
                    self.y += 5
                return True
        else:
            return False

    
        
        

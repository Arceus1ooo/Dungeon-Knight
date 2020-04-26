import pygame
from GlobalVariables import *


# This trigger switches which room is displayed, i.e. player moves from room1 to room2
class RoomSwitch:
    def __init__(self, x, y, width, height, direction, rooms):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction  # What side of the room it's on
        self.collision = False
        self.rooms = rooms
        self.position = (self.x, self.y)
        self.existence = 0

    def redraw(self, win, mapRoom):
        self.existence = 0
        for room in self.rooms:
            if room == mapRoom:
                self.existence += 1
        if self.existence > 0:
            self.x = self.position[0]
            self.y = self.position[1]
            pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height), 1)
        else:
            self.x = -1000
            self.y = -1000

    def detectCollision(self, obj):
        if (self.x + self.width) > obj.x and self.x < (obj.x + obj.width):
            if (self.y + self.height) > obj.y and self.y < (obj.y + obj.height):
                return True
        else:
            return False

    def trigger(self, mapIndex):
        if self.direction == 'right' and mapIndex < mapYMax:
            return mapIndex + 1
        elif self.direction == 'left' and mapIndex > 0:
            return mapIndex - 1
        elif self.direction == 'up' and mapIndex > 0:
            return mapIndex - 1
        elif self.direction == 'down' and mapIndex < mapXMax:
            return mapIndex + 1
        else:
            return mapIndex

    def postTrigger(self, pWidth, pHeight):  # Determines player position after pressing room switch
        if self.direction == 'left':
            return screenWidth - 20 - pWidth
        elif self.direction == 'right':
            return 20
        elif self.direction == 'up':
            return screenHeight - 20 - pHeight
        else:
            return 20

import pygame
from GlobalVariables import *


# This trigger switches which room is displayed, i.e. player moves from room1 to room2
class RoomSwitch:
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction  # What side of the room it's on

    def redraw(self, win):
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height), 1)

    def trigger(self, x, y):
        if self.direction == 'right':
            return y + 1
        elif self.direction == 'left':
            return y - 1
        elif self.direction == 'up':
            return x + 1
        else:  # Down
            return x - 1

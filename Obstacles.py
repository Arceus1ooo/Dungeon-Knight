import pygame
from GlobalVariables import *


class LWall:
    def __init__(self, x, y, width, height, widthScale, heightScale, rooms, location):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.widthScale = widthScale
        self.heightScale = heightScale
        self.rooms = rooms
        self.location = location
        self.position = (self.x, self.y)
        self.visible = True
        self.components = []
        if self.location == 'topLeft':
            self.components.append((self.x, self.y, self.width, self.height * self.heightScale))
            self.components.append((self.x, self.y, self.width * self.widthScale, self.height))
        elif self.location == 'topRight':
            self.components.append((self.x - self.width, self.y, self.width, self.height * self.heightScale))
            self.components.append((self.x - self.width * self.widthScale, self.y, self.width * self.widthScale, self.height))

    def redraw(self, win):
        for component in self.components:
            pygame.draw.rect(win, white, component, 1)

    def detectCollision(self, player):
        for component in self.components:
            if (component[0] + component[2]) > player.x and component[0] < (player.x + player.width):
                if (component[1] + component[3]) > player.y and component[1] < (player.y + player.height):
                    if self.location == 'topLeft':
                        if player.direction == 'left':
                            player.x += player.speed
                        elif player.direction == 'up':
                            player.y += player.speed
                    elif self.location == 'topRight':
                        if player.direction == 'right':
                            player.x -= player.speed
                        elif player.direction == 'up':
                            player.y += player.speed
                    return True
            else:
                return False

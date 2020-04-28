import pygame
from GlobalVariables import *


class LWall:
    def __init__(self, x, y, width, height, widthScale, heightScale, rooms, location):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scaledWidth = width * widthScale
        self.scaledHeight = height * heightScale
        self.rooms = rooms
        self.location = location
        self.position = (self.x, self.y)
        self.visible = True
        self.components = []
        if self.location == 'topLeft':
            self.components.append((self.x, self.y, self.width, self.scaledHeight))
            self.components.append((self.x, self.y, self.scaledWidth, self.height))
        elif self.location == 'topRight':
            self.components.append((self.x - self.width, self.y, self.width, self.scaledHeight))
            self.components.append((self.x - self.scaledWidth, self.y, self.scaledWidth, self.height))
        elif self.location == 'bottomLeft':
            self.components.append((self.x, self.y - self.height, self.scaledWidth, self.height))
            self.components.append((self.x, self.y - self.scaledHeight, self.width, self.height))
        else:
            self.components.append((self.x - self.width, self.y - self.scaledHeight, self.width, self.scaledHeight))
            self.components.append((self.x - self.scaledWidth, self.y - self.height, self.scaledWidth, self.height))

    def redraw(self, win):
        for component in self.components:
            pygame.draw.rect(win, white, component, 1)

    def detectCollision(self, player):
        for x, y, width, height in self.components:
            if (x + width) > player.x and x < (player.x + player.width):
                if (y + height) > player.y and y < (player.y + player.height):
                    if player.direction == 'up':
                        player.y += player.speed
                    elif player.direction == 'down':
                        player.y -= player.speed
                    elif player.direction == 'left':
                        player.x += player.speed
                    else:
                        player.x -= player.speed
                    return True
            else:
                return False

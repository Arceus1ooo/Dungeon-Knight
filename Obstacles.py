import pygame
from GlobalVariables import *


class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alpha = 255

    def detectCollision(self, player):
        if (self.x + self.width) > player.x and self.x < (player.x + player.width):
            if (self.y + self.height) > player.y and self.y < (player.y + player.height):
                if player.direction == 'up':
                    player.y += player.speed
                elif player.direction == 'down':
                    player.y -= player.speed
                elif player.direction == 'left':
                    player.x += player.speed
                else:
                    player.x -= player.speed
        else:
            return False

    def detectRectCollision(self, sprite):
        if (self.x + self.width) > sprite.rect.x and self.x < (sprite.rect.x + sprite.width):
            if (self.y + self.height) > sprite.rect.y and self.y < (sprite.rect.y + sprite.height):
                return True
        else:
            return False


class LWall(Wall):
    def __init__(self, x, y, width, height, widthScale, heightScale, location):
        super().__init__(x, y, width, height)
        self.scaledWidth = width * widthScale
        self.scaledHeight = height * heightScale
        self.location = location
        self.components = []
        self.alpha = 255
        if self.location == 'topLeft':
            self.components.append((self.x, self.y, self.width, self.scaledHeight))
            self.components.append((self.x, self.y, self.scaledWidth, self.height))
        elif self.location == 'topRight':
            self.components.append((self.x - self.width, self.y, self.width, self.scaledHeight))
            self.components.append((self.x - self.scaledWidth, self.y, self.scaledWidth, self.height))
        elif self.location == 'bottomLeft':
            self.components.append((self.x, self.y - self.scaledHeight, self.width, self.scaledHeight))
            self.components.append((self.x, self.y - self.height, self.scaledWidth, self.height))
        else:
            self.components.append((self.x - self.width, self.y - self.scaledHeight, self.width, self.scaledHeight))
            self.components.append((self.x - self.scaledWidth, self.y - self.height, self.scaledWidth, self.height))

    def redraw(self, win, void):
        for component in self.components:
            pygame.draw.rect(win, white, component, 1)

    def detectCollision(self, player):
        for x, y, width, height in self.components:
            if (x + width) > player.x and x < (player.x + player.width):
                if (y + height) > player.y and y < (player.y + player.height):
                    if player.existence > 0:
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

    def detectRectCollision(self, sprite):
        for x, y, width, height in self.components:
            if (x + width) > sprite.rect.x and x < (sprite.rect.x + sprite.width):
                if (y + height) > sprite.rect.y and y < (sprite.rect.y + sprite.height):
                    if sprite.rect.direction == 'up':
                        sprite.rect.y += sprite.rect.speed
                    elif sprite.rect == 'down':
                        sprite.rect.y -= sprite.rect.speed
                    elif sprite.rect.direction == 'left':
                        sprite.rect.x += sprite.rect.speed
                    else:
                        sprite.rect.x -= sprite.rect.speed
                    return True
            else:
                return False


class Barricade(Wall):
    def __init__(self, x, y, width, height, color, rooms):
        super().__init__(x, y, width, height)
        self.color = color
        self.rooms = rooms
        self.existence = 0
        self.position = (self.x, self.y)

    def redraw(self, win, mapRoom):
        self.existence = 0
        for room in self.rooms:
            if room == mapRoom:
                self.existence += 1
        if self.existence > 0:
            self.x = self.position[0]
            self.y = self.position[1]
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 1)
        else:
            self.x = -1000
            self.y = -1000

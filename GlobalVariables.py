# These variables are applied to every script, make sure the names are unique

# Window properties
screenWidth = 500
screenHeight = 480
frameSpeed = 9

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# The map
mainRoom = 'rooms/intro.jpg'
room1 = 'rooms/ex1.jpg'
map = [['null', 'null', 'null'],
       ['null', mainRoom, room1],
       ['null', 'null', 'null']]
# Setting start position
mapX = 1
mapY = 1
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
mapXMax = 2
mapYMax = 2

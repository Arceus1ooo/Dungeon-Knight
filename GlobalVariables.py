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

# Map Initialization
mainRoom = 'rooms/intro.jpg'
room1 = 'rooms/ex1.jpg'
room2 = 'rooms/ex2.jpg'
room3 = 'rooms/ex3.jpg'
room4 = 'rooms/ex4.jpg'
room5 = 'rooms/ex5.jpg'
room6 = 'rooms/ex6.jpg'
room7 = 'rooms/ex7.jpg'
room8 = 'rooms/ex8.jpg'

map = [[room1, room2, room3],
       [room4, mainRoom, room5],
       [room6, room7, room8]]
# Setting start position
mapX = 1
mapY = 1
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
mapXMax = 2
mapYMax = 2

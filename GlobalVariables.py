# These variables are applied to every script, make sure the names are unique

# Window properties
screenWidth = 960
screenHeight = 680
frameSpeed = 9

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)

# Map Initialization
mainRoom = 'rooms/MainRoom.jpg'
room1 = 'rooms/LeftTopRoom.jpg'
room2 = 'rooms/MidTopRoom.jpg'
room3 = 'rooms/RightTopRoom.jpg'
room4 = 'rooms/LeftMidRoom.jpg'
room5 = 'rooms/RightMidRoom.jpg'
room6 = 'rooms/LeftBottomRoom.jpg'
room7 = 'rooms/MidBottomRoom.jpg'
room8 = 'rooms/RightBottomRoom.jpg'

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
swordWidth = 5
swordHeight = 4

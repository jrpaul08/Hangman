import pygame
pygame.font.init()

#window info
WIDTH = 1000
HEIGHT = 500
FPS = 60

#color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,48,48)
BLUE = (30,144,255)
GREEN = (0,201,87)
YELLOW = (255,215,0)

#circle
GAP = 15
RADIUS = 20
A = 65
LETTER_FONT = pygame.font.SysFont('comisans', 40)

FINISH_FONT = pygame.font.SysFont('John Hubbard', 80)

STARTX = round((WIDTH - (GAP + RADIUS*2)*13) / 2)
STARTY = 400

X, Y = 300, 180
LENGTH = 30
SPACE= 40
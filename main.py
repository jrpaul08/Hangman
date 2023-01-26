import pygame
import os
import math


pygame.font.init()
pygame.get_init()

WIDTH, HEIGHT = 800, 500
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,48,48)
BLUE = (30,144,255)

#button
#calculation: (width - (Gap + r*2)*13)/2
RADIUS = 20
GAP = 15

letters = []   #stores triplets   ex: [50, 65, "A"]
startx = round((WIDTH - (GAP + RADIUS*2)*13) / 2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP*2 + ((RADIUS * 2 + GAP) * (i% 13))
    y = starty + ((i//13) * (GAP + RADIUS*2))
    letters.append([x,y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('comisans', 40)

images = []
for i in range(7):
    image = pygame.image.load("images/hangman"+str(i)+".png")
    images.append(image)

hangman_status = 0   #represents which picture of hangman we are at


run = True
clock = pygame.time.Clock()

def draw():
    win.fill(WHITE)  # fill screen with the color white

    for letter in letters:
        x, y, ltr, visible = letter
        if visible == True:
            pygame.draw.circle(win, BLUE, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, RED)
            win.blit(text, (x - RADIUS/2, y - RADIUS/2))

    win.blit(images[hangman_status], (150, 80))
    pygame.display.update()



while run:
    clock.tick(FPS)
    draw()
    win.blit(images[hangman_status], (150, 80))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: #checks if user clicked the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        print(ltr)




pygame.quit()
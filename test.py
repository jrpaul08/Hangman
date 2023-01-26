import random

from pygame import *
from assets.gameSetup import *
from assets.vocabulary import *
import math
pygame.font.init()
pygame.init()



win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")


def menu():
    click = False
    clock = pygame.time.Clock()
    button1 = pygame.Rect(WIDTH / 2 - 200 / 2, 100, 200, 50)  # x pos, y pos,length, height
    button2 = pygame.Rect(WIDTH / 2 - 200 / 2, 200, 200, 50)
    button3 = pygame.Rect(WIDTH / 2 - 200 / 2, 300, 200, 50)
    button4 = pygame.Rect(WIDTH / 2 - 200 / 2, 400, 200, 50)
    text1 = LETTER_FONT.render("Animals", True, (0, 0, 0))
    text2 = LETTER_FONT.render("Fruits", True, (0, 0, 0))
    text3 = LETTER_FONT.render("Vegetables", True, (0, 0, 0))
    text4 = LETTER_FONT.render("Countries", True, (0, 0, 0))

    border1 = pygame.Rect(WIDTH / 2 - 210 / 2, 95, 210, 60)
    border2 = pygame.Rect(WIDTH / 2 - 210 / 2, 195, 210, 60)
    border3 = pygame.Rect(WIDTH / 2 - 210 / 2, 295, 210, 60)
    border4 = pygame.Rect(WIDTH / 2 - 210 / 2, 395, 210, 60)


    while True:
        clock.tick(FPS)
        win.fill((255, 255, 255))
        text = FINISH_FONT.render("Main Menu", True, (0, 0, 0))
        pygame.draw.rect(win, (0, 0, 0), border1)
        pygame.draw.rect(win, (0, 0, 0), border2)
        pygame.draw.rect(win, (0, 0, 0), border3)
        pygame.draw.rect(win, (0, 0, 0), border4)

        pygame.draw.rect(win, (255, 0, 0), button1)
        pygame.draw.rect(win, (255, 0, 0), button2)
        pygame.draw.rect(win, (255, 0, 0), button3)
        pygame.draw.rect(win, (255, 0, 0), button4)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, 25))
        win.blit(text1, (WIDTH / 2 - 100 / 2, 110))
        win.blit(text2, (WIDTH / 2 - 85 / 2, 215))
        win.blit(text3, (WIDTH / 2 - 135 / 2, 310))
        win.blit(text4, (WIDTH / 2 - 120 / 2, 410))

        mx, my = pygame.mouse.get_pos()


        if button1.collidepoint((mx, my)):
            if click:
                game(animals)
        if button2.collidepoint((mx, my)):
            if click:
                game(fruits)
        if button3.collidepoint((mx, my)):
            if click:
                game(vegetables)
        if button4.collidepoint((mx, my)):
            if click:
                game(countries)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def game(theme):
    w = random.choice(theme)
    word = Word(w, win)
    word.setImages()
    word.setButtons()
    word.setLetters()

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        word.drawButtons()
        word.draw_lines()
        word.displayHangman()
        word.displayCorrectLetters()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                for lb in word.buttons:
                    x, y, letter, visibility = lb
                    if visibility:
                        distance = math.sqrt((x - x_mouse)**2 + (y - y_mouse)**2)
                        if distance < RADIUS:
                            if not word.checkLetter(letter):
                                word.hangman_status += 1
                            lb[3] = False

        word.win_game()
        word.lost_game()
        pygame.display.update()

menu()
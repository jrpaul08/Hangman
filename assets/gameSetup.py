import pygame
import time
from assets.constants import *


class Word:

    def __init__(self, word, win):
        self.images = []
        self.hangman_status = 0
        self.word = word
        self.win = win
        self.lineInfo = []
        self.letterStore = []  # start position of line, end position of line, letter
        self.correctLetters = []
        self.buttons = []
        self.winner = False

    '''
    def createLines(self):
        start = self.start_x
        end = self.start_x + self.LENGTH
        for i in range(len(self.word)):
            self.letterStore.append([start, self.y, self.word[i], False])

            pygame.draw.line(self.win, BLACK, (start, self.y), (end, self.y), 5)
            start = end + self.GAP
            end = start + self.LENGTH
        self.letterStore = self.letterStore[:len(self.word)]
    '''

    def setImages(self):
        for i in range(7):
            self.images.append(pygame.image.load("images/hangman" + str(i) + ".png"))

    def setButtons(self):
        for i in range(26):
            x = STARTX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = STARTY + ((i // 13) * (GAP + RADIUS * 2))
            self.buttons.append([x, y, chr(A + i), True])

    def setLetters(self):
        start = X
        end = X + LENGTH
        for i in range(len(self.word)):
            self.letterStore.append([start, Y, self.word[i], False])
            self.lineInfo.append([(start, Y), (end, Y)])
            start = end + SPACE
            end = start + LENGTH

    def drawButtons(self):
        self.win.fill(WHITE)
        for lb in self.buttons:
            x, y, letter, visibility = lb
            if visibility:
                pygame.draw.circle(self.win, BLUE, (x, y), RADIUS, 3)
                text = LETTER_FONT.render(letter, 1, RED)
                self.win.blit(text, (x - RADIUS / 2, y - RADIUS / 2))

    def draw_lines(self):
        for i in (self.lineInfo):
            pygame.draw.line(self.win, BLACK, i[0], i[1], 5)

    def displayHangman(self):
        self.win.blit(self.images[self.hangman_status], (100, 80))

    def checkLetter(self, letter):
        x_offset = 7
        y_offset = -30
        guess = False
        for arr in self.letterStore:
            if arr[2] == letter:
                guess = True
                arr[3] = True
                text = LETTER_FONT.render(letter, True, RED)
                self.correctLetters.append([arr[0] + x_offset, arr[1] + y_offset, text])
        if guess:
            return True
        return False

    def displayCorrectLetters(self):
        for w in self.correctLetters:
            x, y, text = w
            self.win.blit(text, (x, y))

    def win_game(self):
        for i in self.letterStore:
            if not i[3]:
                return
        pygame.time.delay(500)
        self.win.fill(GREEN)
        text = FINISH_FONT.render("YOU WON!", True, YELLOW)
        text2 = LETTER_FONT.render("The word was " + str(self.word), True, BLACK)
        self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 50))
        self.win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT // 2))

    def lost_game(self):
        if self.hangman_status == 6:
            pygame.time.delay(500)
            self.win.fill(RED)
            text = FINISH_FONT.render("YOU LOST :(", True, BLACK)
            text2 = LETTER_FONT.render("The word was " + str(self.word), True, BLACK)
            self.win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 50))
            self.win.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT // 2))

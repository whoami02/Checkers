import pygame
from .constants import BLACK, GREEN, RED, SQUARE_SIZE, WHITE, CROWN

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.rad = SQUARE_SIZE//2 - 10   # 10 is the padding from the square
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
        # if(self.color == WHITE):
        #     self.direction = 1
        # else:
        #     self.direction = -1
    
    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True

    def draw(self, win):
        # pygame.draw.circle(win, BLACK, (self.x, self.y), rad + 2)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2 ))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
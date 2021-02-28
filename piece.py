import pygame
import os

#import black and white  piece images
black_pawn = pygame.image.load(os.path.join("images", "bP.png"))
black_rook = pygame.image.load(os.path.join("images", "bR.png"))
black_horse = pygame.image.load(os.path.join("images", "bN.png"))
black_bishop = pygame.image.load(os.path.join("images", "bB.png"))
black_queen = pygame.image.load(os.path.join("images", "bQ.png"))
black_king = pygame.image.load(os.path.join("images", "bK.png"))

white_pawn = pygame.image.load(os.path.join("images", "wP.png"))
white_rook = pygame.image.load(os.path.join("images", "wR.png"))
white_horse = pygame.image.load(os.path.join("images", "wN.png"))
white_bishop = pygame.image.load(os.path.join("images", "wB.png"))
white_queen = pygame.image.load(os.path.join("images", "wQ.png"))
white_king = pygame.image.load(os.path.join("images", "wK.png"))

black_pieces = [black_pawn, black_rook, black_horse, black_bishop, black_queen, black_king]
white_pieces = [white_pawn, white_rook, white_horse, white_bishop, white_queen, white_king]

Black = []
White = []

for img in black_pieces:
    Black.append(pygame.transform.scale(img, (55, 55)))

for img in white_pieces:
    White.append(pygame.transform.scale(img, (55, 55)))

class Piece(object):


    def __init__(self, row, col, color, img):
        self.row = row
        self.col = col
        self.color = color
        self.img = img
        self.selected = False
        self.move_list = []

    def is_selected(self):
        return self.selected

    def draw(self, windows,x,y):
        if self.color == "white":
            drawThis = White[self.img]
        else:
            drawThis = Black[self.img]

        if self.selected and self.color == color:
            pygame.draw.rect(windows, 0, (x+20, y+20, 62, 62), 2)

        windows.blit(drawThis, (x+20, y+20))


    def update_position(self, r, c):
        self.row = r
        self.col = c

    def get_color(self):
        return self.color

    def get_position(self):
        return self.row, self.col

    def get_possible_moves(self, board):
        self.move_list = self.valid_moves(board)



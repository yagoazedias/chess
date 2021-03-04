import pygame


class House:

    def __init__(self, row, column, color):
        self.column = column
        self.row = row
        self.position_column = (column * 100)
        self.position_row = (row * 100)
        self.color = color
        self.piece = None

    def get_position_column(self):
        return self.position_column

    def get_position_row(self):
        return self.position_row
    
    def set_piece(self,piece):
        self.piece = piece

    def draw(self, display):
        pygame.draw.rect(display, self.color, (self.position_row, self.position_column, 100, 100))
        if self.piece != None:
            self.piece.draw(display,self.position_row, self.position_column)
    

    def get_piece(self):
        return self.piece
    
    def is_empty(self):
        return self.piece == None

# from models.move import Move
from piece import Piece
from move_utils import *

class Knight(Piece):
    def __init__(self, row, col, color, img):
        super(Knight, self).__init__(row, col, color, img)

    def __str__(self):
     return "Knight"

    #-- Metodos auxiliares --#

    # retorna os 2 L's: |--
    def knight_left_L(self, pos):
        row = pos[0]
        col = pos[1]
        l_up = (row-1, col-2)
        l_down = (row+1, col-2)
        return [l_up, l_down]

    # retorna os 2 L's: --|
    def knight_right_L(self, pos):
        row = pos[0]
        col = pos[1]
        r_up = (row-1, col+2)
        r_down = (row+1, col+2)
        return [r_up, r_down]

    # retorna os 2 L's: _|_
    def knight_down_L(self, pos):
        row = pos[0]
        col = pos[1]
        d_left = (row+2, col-1)
        d_right = (row+2, col+1)
        return [d_left, d_right]

    # retorna os 2 L's: T
    def knight_up_L(self, pos):
        row = pos[0]
        col = pos[1]
        u_left = (row-2, col-1)
        u_right = (row-2, col+1)
        return [u_left, u_right]

    #-- --#

    def update_possible_moves(self, board):
        self.move_list = []
        pos = self.get_position()
        self.move_list = knight_down_L(pos) + knight_up_L(pos) \
        + knight_left_L(pos) + knight_right_L(pos)

        invalid_moves = []
        for move in self.move_list:
            if not(board.is_valid_pos(move)) or board.has_teammate(move, self.get_color()):
                invalid_moves.append(move)
    
        self.move_list = [x for x in self.move_list if x not in invalid_moves]
        
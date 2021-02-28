# from models.move import Move
from piece import Piece
from models.move_utils import *

class Pawn(Piece):
    def __init__(self, row, col, color, img):
        super(Pawn, self).__init__(row, col, color, img)
        self.first_move = True
        self.is_queen = False
        
    
    def valid_moves(self, board):
        pos = self.get_position()
        moves = []
        if self.get_color() == 'white':
            pawn_move = up
            diag_right_house = up_right(pos)
            diag_left_house = up_left(pos)
        elif self.get_color() == 'black':
            pawn_move = down
            diag_right_house = down_right(pos)
            diag_left_house = down_left(pos)

        move_front = pawn_move(pos)
        if is_valid_pos(move_front) and is_empty(move_front, board):
            moves.append(move_front)
            if self.first_move:
                self.first_move = False
                move_front = pawn_move(move_front)
                if is_valid_pos(move_front) and is_empty(move_front, board):
                    moves.append(move_front)
        
        if is_valid_pos(diag_left_house) and has_oponent(diag_left_house, board):
            moves.append(diag_left_house)

        if is_valid_pos(diag_right_house) and has_oponent(diag_right_house, board):
            moves.append(diag_right_house)

        return moves
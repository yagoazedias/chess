# from models.move import Move
from piece import Piece
from move_utils import pawn_valid_moves

class Pawn(Piece):
    def __init__(self, row, col, color, img):
        super(Pawn, self).__init__(row, col, color, img)
        self.first_move = True
        self.is_queen = False
        
    def valid_moves(self, board):
        moves = pawn_valid_moves(self.get_position(), board, self.get_color(), self.first_move)
        return moves
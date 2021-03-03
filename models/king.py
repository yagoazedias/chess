# from models.move import Move
from piece import Piece
from move_utils import *


class King(Piece):
    def __init__(self, row, col, color, img):
        super(King, self).__init__(row, col, color, img)
        self.is_first_move = True
        self.is_checked = False

    def __str__(self):
        return "King"

    def set_is_first_move(self, value):
        self.is_first_move = value

    def get_is_first_move(self):
        return self.is_first_move

    def set_is_checked(self, value):
        self.is_checked = value

    def get_is_checked(self):
        return self.is_checked

    def update_possible_moves(self, board):
        self.move_list = []
        pos = self.get_position()
        self.move_list = [up(pos), down(pos), left(pos), right(pos), up_left(pos),
                          up_right(pos), down_left(pos), down_right(pos)]

        invalid_moves = []
        for move in self.move_list:
            if not (board.is_valid_pos(move)) or board.has_teammate(move, self.get_color()):
                invalid_moves.append(move)

        self.move_list = [x for x in self.move_list if x not in invalid_moves]

        # Roque 
        if self.is_first_move and not self.is_checked:
            # Torre da direita
            if board.get_piece((self.row, self.col + 3)) == "Rook" and board.get_piece(
                    (self.row, self.col + 3)).get_is_first_move():
                if board.is_empty(right(pos)) and board.is_empty(right(right(pos))):
                    self.move_list.append(right(right(pos)))
            # Torre da esquerda
            if board.get_piece((self.row, self.col - 4)) == "Rook" and board.get_piece(
                    (self.row, self.col - 4)).get_is_first_move():
                if board.is_empty(left(pos)) and board.is_empty(left(left(pos))) and board.is_empty(
                        left(left(left(pos)))):
                    self.move_list.append(left(left(pos)))

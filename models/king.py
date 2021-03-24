# from models.move import Move
from models.piece import Piece
from util.move import *
from constants.types import ROOK


class King(Piece):
    def __init__(self, col, row, color, img, house):
        super(King, self).__init__(col, row, color, img, house)
        self.is_first_move = True
        self.is_checked = False


    #verifica se o movimento eh o roque.
    #eh roque quando o rei anda mais de uma casa
    def is_special_move(self, current_pos, desired_pos):
        return (abs(current_pos[0] - desired_pos[0]) > 1)
    
    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "King"

    def toggle_first_move(self):
        self.is_first_move = False

    def get_is_first_move(self):
        return self.is_first_move
    

    def get_is_first_move(self):
        return self.is_first_move

    def set_is_checked(self, value):
        self.is_checked = value

    def get_is_checked(self):
        return self.is_checked

    def update_possible_moves(self, board):
        self.move_list = []
        pos = self.house.get_position()
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
            if board.houses[self.col + 3][self.row].get_piece() is not None:
                if board.get_piece((self.col + 3, self.row)).get_type() == ROOK and board.get_piece(
                        (self.col + 3, self.row)).get_is_first_move():
                    if board.is_empty(right(pos)) and board.is_empty(right(right(pos))):
                        self.move_list.append(right(right(pos)))
            # Torre da esquerda
            if board.houses[self.col - 4][self.row].get_piece() is not None:
                if board.get_piece((self.col - 4, self.row)).get_type() == ROOK and board.get_piece(
                        (self.col - 4, self.row)).get_is_first_move():
                    if board.is_empty(left(pos)) and board.is_empty(left(left(pos))) and board.is_empty(
                            left(left(left(pos)))):
                        self.move_list.append(left(left(pos)))

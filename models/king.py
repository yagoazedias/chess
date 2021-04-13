from models.piece import Piece
from constants.types import ROOK
from util.move import *
from constants.colors import *


class King(Piece):
    def __init__(self, color, img, house):
        super(King, self).__init__(color, img, house)
        self.is_first_move = True
        self.turn_first_move_false = 0
        self.is_checked = False

        
    def get_value(self):
        if self.get_color() == WHITE:
            return 150
        else:
            return -150

    # verifica se o movimento eh o roque.
    # eh roque quando o rei anda mais de uma casa
    def is_special_move(self, current_pos, desired_pos):
        return abs(current_pos[0] - desired_pos[0]) > 1

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "King"

    def set_is_first_move(self, condition, turn):
        self.is_first_move = condition
        self.turn_first_move_false = turn

    def get_is_first_move(self):
        return self.is_first_move
    
    def get_turn_first_move_false(self):
        return self.turn_first_move_false

    def set_is_checked(self, value):
        self.is_checked = value

    def get_is_checked(self):
        return self.is_checked

    def update_possible_moves(self, match):
        self.move_list = []
        pos = self.house.get_position()
        self.move_list = [up(pos), down(pos), left(pos), right(pos), up_left(pos),
                          up_right(pos), down_left(pos), down_right(pos)]

        invalid_moves = []
        for move in self.move_list:
            if not (is_valid_pos(move)) or has_teammate(move, self.get_color(), match.board):
                invalid_moves.append(move)

        self.move_list = [x for x in self.move_list if x not in invalid_moves]

        # Roque 
        if self.is_first_move and not self.is_checked:
            
            col = self.house.get_position()[0]
            row = self.house.get_position()[1]
            # Torre da direita
            if match.board.houses[col + 3][row].get_piece() is not None:
                if match.board.get_piece((col + 3, row)).get_type() == ROOK and match.board.get_piece(
                        (col + 3, row)).get_is_first_move():
                    if match.board.is_empty(right(pos)) and match.board.is_empty(right(right(pos))):
                        self.move_list.append(right(right(pos)))
            # Torre da esquerda
            if match.board.houses[col - 4][row].get_piece() is not None:
                if match.board.get_piece((col - 4, row)).get_type() == ROOK and match.board.get_piece(
                        (col - 4, row)).get_is_first_move():
                    if match.board.is_empty(left(pos)) and match.board.is_empty(
                            left(left(pos))) and match.board.is_empty(
                            left(left(left(pos)))):
                        self.move_list.append(left(left(pos)))

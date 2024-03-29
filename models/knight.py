from models.piece import Piece
from util.move import *
from constants.colors import *


class Knight(Piece):
    def __init__(self, color, img, house):
        super(Knight, self).__init__(color, img, house)

    
    def get_value(self):
        if self.get_color() == WHITE:
            return 29
        else:
            return -29

    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Knight"

    # -- Metodos auxiliares --#

    # retorna os 2 L's: |--
    def knight_left(self):
        col = self.house.get_position()[0]
        row = self.house.get_position()[1]
        l_up = (col - 2, row - 1)
        l_down = (col - 2, row + 1)
        return [l_up, l_down]

    # retorna os 2 L's: --|
    def knight_right(self):
        col = self.house.get_position()[0]
        row = self.house.get_position()[1]
        r_up = (col + 2, row - 1)
        r_down = (col + 2, row + 1)
        return [r_up, r_down]

    # retorna os 2 L's: _|_
    def knight_down(self):
        col = self.house.get_position()[0]
        row = self.house.get_position()[1]
        d_left = (col - 1, row + 2)
        d_right = (col + 1, row + 2)
        return [d_left, d_right]

    # retorna os 2 L's: T
    def knight_up(self):
        col = self.house.get_position()[0]
        row = self.house.get_position()[1]
        u_left = (col - 1, row - 2)
        u_right = (col + 1, row - 2)
        return [u_left, u_right]

    # -- --#

    def update_possible_moves(self, match):
        self.move_list = []
        pos = self.house.get_position()
        self.move_list = self.knight_down() + self.knight_up() + self.knight_left() + self.knight_right()

        invalid_moves = []
        for move in self.move_list:
            if not (is_valid_pos(move)) or has_teammate(move, self.get_color(), match.board):
                invalid_moves.append(move)

        self.move_list = [x for x in self.move_list if x not in invalid_moves]

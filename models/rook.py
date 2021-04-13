from models.piece import Piece
from util.move import *
from constants.colors import *



class Rook(Piece):
    def __init__(self, color, img, house):
        super(Rook, self).__init__(color, img, house)
        self.is_first_move = True
        self.turn_first_move_false = 0


    def get_value(self):
        if self.get_color() == WHITE:
            return 50
        else:
            return -50


    def get_type(self):
        return self.__str__()

    def __str__(self):
        return "Rook"
    
    def set_is_first_move(self, condition, turn):
        self.is_first_move = condition
        self.turn_first_move_false = turn

    def get_is_first_move(self):
        return self.is_first_move
    
    def get_turn_first_move_false(self):
        return self.turn_first_move_false

    def update_possible_moves(self, match):
        pos = self.house.get_position()
        self.move_list = all_down_moves(pos, match, self.color) + \
                         all_up_moves(pos, match, self.color) + \
                         all_right_moves(pos, match, self.color) + \
                         all_left_moves(pos, match, self.color)

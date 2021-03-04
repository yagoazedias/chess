# from models.move import Move
from models.piece import Piece
from util.move import *


class Pawn(Piece):
    def __init__(self, row, col, color, img):
        super(Pawn, self).__init__(row, col, color, img)
        self.first_move = True
        # self.is_queen = False
        self.is_en_passant_vulnerable = False

    def __str__(self):
        return "Pawn"

    def update_possible_moves(self, board):
        self.move_list = []
        pos = self.get_position()
        if self.get_color() == 'white':
            pawn_move = up
            diag_right_house = up_right(pos)
            diag_left_house = up_left(pos)
        # elif self.get_color() == 'black'
        else:
            pawn_move = down
            diag_right_house = down_right(pos)
            diag_left_house = down_left(pos)

        move_front = pawn_move(pos)
        if board.is_valid_pos(move_front) and board.is_empty(move_front):
            self.move_list.append(move_front)
            if self.first_move:
                move_front = pawn_move(move_front)
                if board.is_valid_pos(move_front) and board.is_empty(move_front):
                    self.move_list.append(move_front)

        # Movimentos de captura normais
        if board.is_valid_pos(diag_left_house) and board.has_opponent(diag_left_house, self.color):
            self.move_list.append(diag_left_house)

        if board.is_valid_pos(diag_right_house) and board.has_opponent(diag_right_house, self.color):
            self.move_list.append(diag_right_house)

        # Movimentos de captura en passant

        # se à direita do meu peão tiver um peão adversario
        if board.is_valid_pos(right(pos)) and board.get_piece(right(pos)) == 'Pawn':
            # e se este peão estiver vulnerável à captura en passant
            if board.get_piece(right(pos)).get_en_passant_vulnerable():
                # e se a posicao atras desse peão estiver vazia
                if board.is_valid_pos(diag_right_house) and board.is_empty(diag_right_house):
                    self.move_list.append(diag_right_house)

        if board.is_valid_pos(left(pos)) and board.get_piece(left(pos)) == 'Pawn':
            if board.get_piece(left(pos)).get_en_passant_vulnerable():
                if board.is_valid_pos(diag_left_house) and board.is_empty(diag_left_house):
                    self.move_list.append(diag_left_house)

    def set_is_en_passant_vulnerable(self, value):
        self.is_en_passant_vulnerable = value

    def get_en_passant_vulnerable(self, value):
        return self.is_en_passant_vulnerable

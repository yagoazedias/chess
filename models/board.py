import pygame
from models.house import House
from constants.colors import *

from models.king import King
from models.queen import Queen
from models.rook import Rook
from models.bishop import Bishop
from models.knight import Knight as Horse
from models.pawn import Pawn

from constants import images

class Board:
    def __init__(self):
        self.prepare_board()

    def prepare_board(self):
        self.turn = WHITE
        self.winner = None
        self.houses = self.build_houses()
        self.set_up_pieces()

    def get_selected_house(self):
        for col in range(0, 8):
            for row in range(0, 8):
                if self.houses[col][row].get_piece():
                    if self.houses[col][row].get_piece().is_selected():
                        return self.houses[col][row]
        return None

    def unselect_selected_house(self):
        selected_house = self.get_selected_house()
        selected_house.get_piece().set_selected(False)


    def draw(self, display, text_font):
        self.prepare_player_turn_indicator(display, text_font, 100, 410)
        for col in range(0, 8):
            for row in range(0, 8):
                self.houses[col][row].draw(display)

    def clean_high_light(self):
        for col in range(0, 8):
            for row in range(0, 8):
                self.houses[col][row].set_is_high_light(False)

    def build_houses(self):
        houses = [[0 for _ in range(8)] for __ in range(8)]
        for col in range(0, 8):
            color_index = col % 2
            for row in range(0, 8):
                color = WHITE if color_index == 0 else BLACK
                houses[col][row] = House(col, row, color)
                color_index = (color_index + 1) % 2
        return houses

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

    def move_piece(self):
        print("move_piece")

    def get_house(self, pos):
        col = pos[0]
        row = pos[1]
        return self.houses[col][row]

    # verifica se a posicao pos tem um oponente
    def has_opponent(self, pos, piece_color):
        if self.get_house(pos).get_piece() == None:
            return False
        return piece_color != self.get_house(pos).get_piece().get_color()

    # verifica se a posicao pos é valida. ou seja, esta dentro dos limites do tabuleiro
    def is_valid_pos(self, pos):
        col = pos[0]
        row = pos[1]
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_piece(self, pos):
        return self.get_house(pos).get_piece()

    def is_empty(self, pos):
        return self.get_house(pos).is_empty()

    # verifica se a posicao pos tem um companheiro de equipe
    def has_teammate(self, pos, my_color):
        if not self.is_valid_pos(pos):
            return False
        if self.get_house(pos).get_piece() == None:
            return False
        return my_color == self.get_house(pos).get_piece().get_color()
    
    def get_turn(self):
        return self.turn
    
    def switch_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
            
    def prepare_player_turn_indicator(self, screen, font, x, y):
        self.clean_turn_indicator(screen)
        self.draw_button(screen,font)
        text = "Vez das peças "
        if self.turn == WHITE:
            text += "brancas"
            color = WHITE
        else:
            text += "pretas"
            color = (0, 0, 0)
        indicator = font.render(text, True, color)

        screen_width = screen.get_width() / 2
        text_width = indicator.get_width() / 2
        x = screen_width - text_width

        screen.blit(indicator, (x, y))
        
    def clean_turn_indicator(self, screen):
        pygame.draw.rect(screen, (26,120,122), (0, 400, 400, 100))
        
    def draw_button(self, screen, font):
        height = 25
        width = 200
        x = screen.get_width() / 4
        y = 440
        text = "Reiniciar Partida"
        
        pygame.draw.rect(screen, (210, 210, 210), (x, y, width, height ), 0, 3, 3, 3, 3)
        textButton = font.render(text, True, (0, 0, 0))
        screen.blit(
            textButton, (x + ((width - textButton.get_width()) / 2), y + height * 0.2)
        )
      
    def set_up_pieces(self):
        self.houses[0][0].set_piece(
            Rook(0, 0, BLACK, images.black_rook, self.houses[0][0])
        )
        self.houses[1][0].set_piece(
            Horse(1, 0, BLACK, images.black_horse, self.houses[1][0])
        )
        self.houses[2][0].set_piece(
            Bishop(2, 0, BLACK, images.black_bishop, self.houses[2][0])
        )
        self.houses[3][0].set_piece(
            Queen(3, 0, BLACK, images.black_queen, self.houses[3][0])
        )
        self.houses[4][0].set_piece(
            King(4, 0, BLACK, images.black_king, self.houses[4][0])
        )
        self.houses[5][0].set_piece(
            Bishop(5, 0, BLACK, images.black_bishop, self.houses[5][0])
        )
        self.houses[6][0].set_piece(
            Horse(6, 0, BLACK, images.black_horse, self.houses[6][0])
        )
        self.houses[7][0].set_piece(
            Rook(7, 0, BLACK, images.black_rook, self.houses[7][0])
        )

        self.houses[0][1].set_piece(
            Pawn(0, 1, BLACK, images.black_pawn, self.houses[0][1])
        )
        self.houses[1][1].set_piece(
            Pawn(1, 1, BLACK, images.black_pawn, self.houses[1][1])
        )
        self.houses[2][1].set_piece(
            Pawn(2, 1, BLACK, images.black_pawn, self.houses[2][1])
        )
        self.houses[3][1].set_piece(
            Pawn(3, 1, BLACK, images.black_pawn, self.houses[3][1])
        )
        self.houses[4][1].set_piece(
            Pawn(4, 1, BLACK, images.black_pawn, self.houses[4][1])
        )
        self.houses[5][1].set_piece(
            Pawn(5, 1, BLACK, images.black_pawn, self.houses[5][1])
        )
        self.houses[6][1].set_piece(
            Pawn(6, 1, BLACK, images.black_pawn, self.houses[6][1])
        )
        self.houses[7][1].set_piece(
            Pawn(7, 1, BLACK, images.black_pawn, self.houses[7][1])
        )

        self.houses[0][7].set_piece(
            Rook(0, 7, WHITE, images.white_rook, self.houses[0][7])
        )
        self.houses[1][7].set_piece(
            Horse(1, 7, WHITE, images.white_horse, self.houses[1][7])
        )
        self.houses[2][7].set_piece(
            Bishop(2, 7, WHITE, images.white_bishop, self.houses[2][7])
        )
        self.houses[3][7].set_piece(
            Queen(3, 7, WHITE, images.white_queen, self.houses[3][7])
        )
        self.houses[4][7].set_piece(
            King(4, 7, WHITE, images.white_king, self.houses[4][7])
        )
        self.houses[5][7].set_piece(
            Bishop(5, 7, WHITE, images.white_bishop, self.houses[5][7])
        )
        self.houses[6][7].set_piece(
            Horse(6, 7, WHITE, images.white_horse, self.houses[6][7])
        )
        self.houses[7][7].set_piece(
            Rook(7, 7, WHITE, images.white_rook, self.houses[7][7])
        )

        self.houses[0][6].set_piece(
            Pawn(0, 6, WHITE, images.white_pawn, self.houses[0][6])
        )
        self.houses[1][6].set_piece(
            Pawn(1, 6, WHITE, images.white_pawn, self.houses[1][6])
        )
        self.houses[2][6].set_piece(
            Pawn(2, 6, WHITE, images.white_pawn, self.houses[2][6])
        )
        self.houses[3][6].set_piece(
            Pawn(3, 6, WHITE, images.white_pawn, self.houses[3][6])
        )
        self.houses[4][6].set_piece(
            Pawn(4, 6, WHITE, images.white_pawn, self.houses[4][6])
        )
        self.houses[5][6].set_piece(
            Pawn(5, 6, WHITE, images.white_pawn, self.houses[5][6])
        )
        self.houses[6][6].set_piece(
            Pawn(6, 6, WHITE, images.white_pawn, self.houses[6][6])
        )
        self.houses[7][6].set_piece(
            Pawn(7, 6, WHITE, images.white_pawn, self.houses[7][6])
        )

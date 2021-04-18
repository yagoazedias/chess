import pygame
from models.house import House
from constants.colors import *
from constants.types import PAWN, ROOK, KING

from models.king import King
from models.queen import Queen
from models.rook import Rook
from models.bishop import Bishop
from models.knight import Knight as Horse
from models.pawn import Pawn
from models.board import Board

from constants import images
from util.move import *


class Match:

    def __init__(self):
        self.prepare_match()

    def prepare_match(self):
        self.winner = None
        self.turn = WHITE
        self.turn_counter = 1
        self.selected_piece_house = None
        self.choice = False
        self.checked = False
        self.is_checkmate = False
        self.is_stalemate = False
        self.board = Board(houses=self.build_houses())
        self.set_up_pieces()


    def get_is_stalemate(self):
        return self.is_stalemate
    
    def get_board(self):
        return self.board

    def draw(self, display, text_font):
        if self.choice:
            if not self.is_checkmate:
                
                if self.get_is_stalemate():
                    draw = images.draw
                    draw_this = pygame.transform.scale(draw, (400,400))
                    display.blit(draw_this, (0, 0))
                    
                else:
                    for col in range(0, 8):
                        for row in range(0, 8):
                            self.board.houses[col][row].draw(display)
            
            else:
                fallen_king = images.fallen_white_king if self.get_turn() == WHITE else images.fallen_black_king
                draw_this = pygame.transform.scale(fallen_king, (400,400))
                display.blit(draw_this, (0, 0))
            self.text_indicator(display, text_font, 100, 410)
            self.draw_button(display, text_font)
        else:
            draw_this = pygame.transform.scale(images.chess, (400,400))
            display.blit(draw_this, (0, 0))

    def build_houses(self):
        houses = [[0 for _ in range(8)] for __ in range(8)]
        for col in range(0, 8):
            color_index = col % 2
            for row in range(0, 8):
                color = WHITE if color_index == 0 else BLACK
                houses[col][row] = House(col, row, color)
                color_index = (color_index + 1) % 2
        return houses
    
    def button_manager(self):
        if self.checked:
            self.checked = False
        else:
            self.prepare_match()

    def get_turn(self):
        return self.turn

    def switch_turn(self):
        self.turn_counter += 1
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def movement_manager(self, selected_house, desired_house):
        
        ia_turn = False            
        
        if desired_house is not None:
            self.board.set_selected_piece_house(selected_house)
            ia_turn = True

        position = selected_house.get_position()
        color_turn = self.get_turn()

        # verifica se há uma peça na casa
        if not self.checked and selected_house.get_piece() is not None and has_teammate(position, color_turn, self.board) and desired_house is None:
            selected_piece = selected_house.get_piece()
            
            # impedir que o rei em xeque faça roque
            if selected_piece.get_type() == KING:
                selected_piece.set_is_checked(self.is_checked(selected_piece.get_color()))
                
            if selected_piece.get_color() == self.get_turn():
                possible_moves = selected_piece.get_possible_moves(self)
                self.board.clean_highlight()
                for possible_move in possible_moves:
                    self.board.houses[possible_move[0]][possible_move[1]].set_is_highlight(True)

                self.board.set_selected_piece_house(selected_house)

        else:
            
            if self.checked and not ia_turn:
                return
        
            self.checked = self.is_checked(self.get_turn())
            
            # verifica se a casa clicada está realçada
            if selected_house.get_is_highlight() or desired_house is not None:

                # casa desejada
                desired_house = selected_house if desired_house is None else desired_house
                
                selected_house = selected_house if desired_house is None else self.board.get_selected_piece_house()

                # peca selecionada
                selected_piece = selected_house.get_piece()
                
                # lógica de movimentação e captura
                captured_piece = self.move(selected_house, desired_house)

                self.checked = self.is_checked(self.get_turn())
                if self.checked:
                    self.undo_move(selected_house, desired_house, captured_piece)

                else:
                    # promocao do peao
                    if selected_piece.get_type() == PAWN and selected_piece.can_be_promoted():
                        if selected_piece.get_color() == BLACK:
                            queen_image = images.black_queen
                        else:
                            queen_image = images.white_queen
                        queen = Queen(selected_piece.get_color(), queen_image, desired_house.get_position())
                        desired_house.set_piece(queen)

                # limpa a casa da peça selecionada
                self.board.set_selected_piece_house(None)

                
                # Troca o turno
                if not self.checked: 
                    self.switch_turn()
                
                # limpar as casas realçadas
                self.board.clean_highlight()


    def move(self, selected_house, desired_house):
        # peça capturada
        captured_piece = desired_house.get_piece()
        # peca selecionada
        selected_piece = selected_house.get_piece()
        # posicao atual
        selected_piece_current_pos = selected_house.get_position()
        # posicao desejada
        selected_piece_desired_pos = desired_house.get_position()

        # en passant
        if selected_piece.get_type() == PAWN:

            # se o peao estiver fazendo seu segundo movimento,
            if not selected_piece.get_is_first_move():
                # ele nao fica mais vulneravel a captura en passant
                selected_piece.set_is_en_passant_vulnerable(False)

            # se o peao fizer o movimento inicial de andar duas casas...
            if selected_piece.is_special_move(selected_piece_current_pos, selected_piece_desired_pos):
                # fica vulneravel ao en passant
                selected_piece.set_is_en_passant_vulnerable(True)

            # se a jogada escolhida for uma captura en passant...
            if (selected_piece.is_en_passant_capture_move(self.board, selected_piece_current_pos,
                selected_piece_desired_pos)):
                # se o meu peao for branco,
                if selected_piece.get_color() == WHITE:
                    # o peao adversario capturado esta 'abaixo' do meu
                    opponent_pawn_house = self.board.get_house(down(selected_piece_desired_pos))

                # se o meu peao for preto,
                else:
                    # o peao adversario capturado esta 'acima' do meu
                    opponent_pawn_house = self.board.get_house(up(selected_piece_desired_pos))

                # remove o peao vulneravel
                captured_piece = opponent_pawn_house.get_piece()
                opponent_pawn_house.set_piece(None)
                
        # roque
        if selected_piece.get_type() == KING:

            # se o movimento escolhido for o roque
            if selected_piece.is_special_move(selected_piece_current_pos, selected_piece_desired_pos):
                
                # roque para esquerda
                if selected_piece_current_pos[0] > selected_piece_desired_pos[0]:
                    rook_current_pos = left(left(left(left(selected_piece_current_pos))))
                    rook_desired_pos = left(selected_piece_current_pos)

                # roque para direita
                else:
                    rook_current_pos = right(right(right(selected_piece_current_pos)))
                    rook_desired_pos = right(selected_piece_current_pos)

                # movimenta a torre
                self.board.get_house(rook_desired_pos).set_piece(
                self.board.get_house(rook_current_pos).get_piece())
                self.board.get_house(rook_current_pos).set_piece(None)

        
        # registra primeiro movimento da peça
        if selected_piece.get_type() == PAWN or selected_piece.get_type() == ROOK or selected_piece.get_type() == KING:
            if selected_piece.get_is_first_move():
                selected_piece.set_is_first_move(False, self.turn_counter)
                   
        desired_house.set_piece(selected_piece)
        selected_house.set_piece(None)    
        return captured_piece
    
    def undo_move(self, origin_house, destiny_house, captured_piece):
        
        # peca selecionada
        selected_piece = destiny_house.get_piece()
        # desfaz o registro do primeiro movimento da peça
        if selected_piece.get_type() == PAWN or selected_piece.get_type() == ROOK or selected_piece.get_type() == KING:
            if self.turn_counter == selected_piece.get_turn_first_move_false():
                selected_piece.set_is_first_move(True, 0)
                
        origin_house.set_piece(destiny_house.get_piece())
        destiny_house.set_piece(None)
        if captured_piece is not None:
            if captured_piece.get_type() == PAWN:
                if captured_piece.get_en_passant_vulnerable():
                    if captured_piece.get_color == WHITE:
                        self.board.houses[destiny_house.get_position()[0]][4].set_piece(captured_piece)
                    else:
                        self.board.houses[destiny_house.get_position()[0]][3].set_piece(captured_piece)
                else:
                   destiny_house.set_piece(captured_piece) 
            else:
                destiny_house.set_piece(captured_piece)
                
    def is_checked(self, color):
        king_position = self.get_king_position()
        for col in range(0, 8):
            for row in range(0, 8):
                if self.board.houses[col][row].get_piece() is not None:
                    if self.board.houses[col][row].get_piece().get_color() != color:
                        possible_moves = self.board.houses[col][row].get_piece().get_possible_moves(self)
                        for possible_move in possible_moves:
                            if possible_move == king_position:
                                return True
        return False
    
    def checkmate(self):
        
        for col in range(0, 8):
            for row in range(0, 8): 
                if self.board.houses[col][row].get_piece() is not None:
                    if self.board.houses[col][row].get_piece().get_color() == self.get_turn():
                        possible_moves = self.board.houses[col][row].get_piece().get_possible_moves(self)
                        all_moves_results_in_check = False
                        for possible_move in possible_moves:
                            captured_piece = self.move(self.board.houses[col][row],self.board.houses[possible_move[0]][possible_move[1]])
                            checked = self.is_checked(self.get_turn()) 
                            self.undo_move(self.board.houses[col][row],self.board.houses[possible_move[0]][possible_move[1]], captured_piece)
                            if not checked:
                                return False
                            
        if not self.is_checked(self.get_turn()):
            self.is_stalemate = True
            return False
                       
        return True

    def get_king_position(self):
        for col in range(0, 8):
            for row in range(0, 8):
                if self.board.houses[col][row].get_piece() is not None:
                    if self.board.houses[col][row].get_piece().get_color() == self.get_turn():
                        if self.board.houses[col][row].get_piece().get_type() == KING:
                            return col, row
        raise ValueError('Não foi encontrado o rei do jogar atual no tabuleiro!')

    def text_indicator(self, screen, font, x, y):
        self.clear_text_indicator(screen)
        text = ""
        color = self.get_turn() if self.get_turn() == WHITE else (0, 0, 0)
        another_color = (0, 0, 0) if self.get_turn() == WHITE else WHITE
        if not self.checked:
            if self.is_checkmate:
                text = "Brancas Venceram!" if self.get_turn() != WHITE else "Pretas Venceram"
                color = another_color
            
            elif self.get_is_stalemate():
                text = "Empate"
                
            else:
                text = "Vez das peças "
                if self.turn != WHITE:
                    text += "pretas"
                else:
                    text += "brancas"
        else:
            text = "Ficou em Xeque! Faça outra jogada."
            
        indicator = font.render(text, True, color)

        screen_width = screen.get_width() / 2
        text_width = indicator.get_width() / 2
        x = screen_width - text_width

        screen.blit(indicator, (x, y))

    def clear_text_indicator(self, screen):
        pygame.draw.rect(screen, (26, 120, 122), (0, 400, 400, 100))

    def draw_button(self, screen, font):
        height = 25
        width = 200
        x = screen.get_width() / 4
        y = 440
        if self.checked:
            text = "Ok"
        else:
            text = "Reiniciar Partida"

        pygame.draw.rect(screen, (210, 210, 210), (x, y, width, height), 0, 3, 3, 3, 3)
        text_button = font.render(text, True, (0, 0, 0))
        screen.blit(
            text_button, (x + ((width - text_button.get_width()) / 2), y + height * 0.2)
        )

    def set_up_pieces(self):
        self.board.houses[0][0].set_piece(Rook(BLACK, images.black_rook, self.board.houses[0][0]))
        self.board.houses[1][0].set_piece(Horse(BLACK, images.black_horse, self.board.houses[1][0]))
        self.board.houses[2][0].set_piece(Bishop(BLACK, images.black_bishop, self.board.houses[2][0]))
        self.board.houses[3][0].set_piece(Queen(BLACK, images.black_queen, self.board.houses[3][0]))
        self.board.houses[4][0].set_piece(King(BLACK, images.black_king, self.board.houses[4][0]))
        self.board.houses[5][0].set_piece(Bishop(BLACK, images.black_bishop, self.board.houses[5][0]))
        self.board.houses[6][0].set_piece(Horse(BLACK, images.black_horse, self.board.houses[6][0]))
        self.board.houses[7][0].set_piece(Rook(BLACK, images.black_rook, self.board.houses[7][0]))

        self.board.houses[0][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[0][1]))
        self.board.houses[1][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[1][1]))
        self.board.houses[2][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[2][1]))
        self.board.houses[3][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[3][1]))
        self.board.houses[4][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[4][1]))
        self.board.houses[5][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[5][1]))
        self.board.houses[6][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[6][1]))
        self.board.houses[7][1].set_piece(Pawn(BLACK, images.black_pawn, self.board.houses[7][1]))

        self.board.houses[0][7].set_piece(Rook(WHITE, images.white_rook, self.board.houses[0][7]))
        self.board.houses[1][7].set_piece(Horse(WHITE, images.white_horse, self.board.houses[1][7]))
        self.board.houses[2][7].set_piece(Bishop(WHITE, images.white_bishop, self.board.houses[2][7]))
        self.board.houses[3][7].set_piece(Queen(WHITE, images.white_queen, self.board.houses[3][7]))
        self.board.houses[4][7].set_piece(King(WHITE, images.white_king, self.board.houses[4][7]))
        self.board.houses[5][7].set_piece(Bishop(WHITE, images.white_bishop, self.board.houses[5][7]))
        self.board.houses[6][7].set_piece(Horse(WHITE, images.white_horse, self.board.houses[6][7]))
        self.board.houses[7][7].set_piece(Rook(WHITE, images.white_rook, self.board.houses[7][7]))
        self.board.houses[0][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[0][6]))
        self.board.houses[1][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[1][6]))
        self.board.houses[2][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[2][6]))
        self.board.houses[3][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[3][6]))
        self.board.houses[4][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[4][6]))
        self.board.houses[5][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[5][6]))
        self.board.houses[6][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[6][6]))
        self.board.houses[7][6].set_piece(Pawn(WHITE, images.white_pawn, self.board.houses[7][6]))

    

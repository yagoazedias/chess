import pygame
from models.board import Board
from constants.types import PAWN, ROOK
from constants.colors import *

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[1] <= 400:
                    movement_manager(board)
                elif restart_button_click_manager(pygame.mouse, screen):
                    board.prepare_board()

        pygame.display.update()
        clock.tick(60)
        board.draw(screen,text_font)


def movement_manager(board):
    
    # seleciona a casa clicada
    selected_house = get_clicked_house(board)
    position = selected_house.get_position()
    color_turn = board.get_turn()
    
    # verifica se há uma peça na casa
    if selected_house.get_piece() is not None and board.has_teammate(position,color_turn):
        selected_piece = selected_house.get_piece()
        if selected_piece.get_color() == board.get_turn():
            possible_moves = selected_piece.get_possible_moves(board)
            board.clean_highlight()
            for possible_move in possible_moves:
                board.houses[possible_move[0]][possible_move[1]].set_is_highlight(True)

            # guarda a casa da peça selecionada
            board.set_selected_piece_house(selected_house)

    
    else:
        # verifica se a casa clicada está realçada
        if selected_house.get_is_highlight():
            
            candidate_house = selected_house

            #lógica que registra que já foi dado o primeiro movimento
            test = board.get_selected_piece_house().get_piece().get_type()
            if test == PAWN:
                board.get_selected_piece_house().get_piece().toggle_first_move()

            # lógica de movimentação e captura
            candidate_house.set_piece(board.get_selected_piece_house().get_piece())
            board.get_selected_piece_house().set_piece(None)
            board.set_selected_piece_house(None)
            board.switch_turn()

            # limpar as casas realçadas
            board.clean_highlight()

def get_clicked_house(board):
    return board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
        int(pygame.mouse.get_pos()[1] / (6.25 * 8))]

def restart_button_click_manager(mouse, screen):
    return (mouse.get_pos()[0] >= screen.get_width() / 4 and mouse.get_pos()[
        0] <= screen.get_width() / 4 + 200 and
            mouse.get_pos()[1] >= 440 and mouse.get_pos()[
                1] <= 440 + 25)

if __name__ == "__main__":
    main()

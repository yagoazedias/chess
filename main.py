import pygame
from models.board import Board
#from models.ia import Ia
from constants.types import PAWN, ROOK, KING
from constants.colors import *
from util.move import *

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    board = Board()
    #ia = Ia(board)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #ia.move()
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
            
            #casa desejada
            desired_house = selected_house
            #peca selecionada
            selected_piece = board.get_selected_piece_house().get_piece()
            #posicao atual
            selected_piece_current_pos = board.get_selected_piece_house().get_position()
            #posicao desejada
            selected_piece_desired_pos = selected_house.get_position()


            # en passant
            if selected_piece.get_type() == PAWN:

                #se o peao estiver fazendo seu segundo movimento,
                if not selected_piece.get_is_first_move():
                    #ele nao fica mais vulneravel a captura en passant
                    selected_piece.set_is_en_passant_vulnerable(False)
                    
                selected_piece.toggle_first_move()

                # se o peao fizer o movimento inicial de andar duas casas...
                if selected_piece.is_special_move(selected_piece_current_pos, selected_piece_desired_pos):
                    #fica vulneravel ao en passant
                    selected_piece.set_is_en_passant_vulnerable(True)
                
                # se a jogada escolhida for uma captura en passant...
                if (selected_piece.is_en_passant_capture_move(board, selected_piece_current_pos, selected_piece_desired_pos)):
                        #se o meu peao for branco,
                        if selected_piece.get_color() == WHITE:
                            #o peao adversario capturado esta 'abaixo' do meu
                            opponent_pawn_house = board.get_house(down(selected_piece_desired_pos))

                        #se o meu peao for preto,
                        else:
                            #o peao adversario capturado esta 'acima' do meu
                            opponent_pawn_house = board.get_house(up(selected_piece_desired_pos))

                        #remove o peao vulneravel
                        opponent_pawn_house.set_piece(None)

            #roque
            if selected_piece.get_type() == KING:
                selected_piece.toggle_first_move()

                #se o movimento escolhido for o roque
                if selected_piece.is_special_move(selected_piece_current_pos, selected_piece_desired_pos):
                    
                    #roque para esquerda
                    if selected_piece_current_pos[0] > selected_piece_desired_pos[0]:
                        rook_current_pos = left(left(left(left(selected_piece_current_pos))))
                        rook_desired_pos = left(selected_piece_current_pos)
                        
                    #roque para direita
                    else:
                        rook_current_pos = right(right(right(selected_piece_current_pos)))
                        rook_desired_pos = right(selected_piece_current_pos)


                    #movimenta a torre
                    board.get_house(rook_desired_pos).set_piece(board.get_house(rook_current_pos).get_piece())
                    board.get_house(rook_current_pos).set_piece(None)


            # lógica de movimentação e captura
            desired_house.set_piece(board.get_selected_piece_house().get_piece())
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

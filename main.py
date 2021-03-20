import pygame
from models.board import Board
from constants.types import PAWN, ROOK
from constants.colors import *

pygame.init()

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()
    buttonTextStart = "Iniciar/Abandonar"

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    # defining button text
    buttonTextStart = "Iniciar/Abandonar"

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

        

        draw_button(screen, buttonTextStart, 25, 200, screen.get_width() / 4, 440)

        pygame.display.update()
        clock.tick(60)
        board.draw(screen,text_font)


def movement_manager(board):
    board.clean_high_light()
    selected_house = board.get_selected_house()

    if selected_house:
        candidate_house = board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
            int(pygame.mouse.get_pos()[1] / (6.25 * 8))
        ]

        # lógica de movimentação e troca de casa da peça
        if (
                candidate_house.get_position()
                in selected_house.get_piece().get_possible_moves(board)
        ):

            # lógica de movimentação sem capitura (troca 'candidate_house' por 'selected_house' e o ultimo é anulado)
            if candidate_house.get_piece() is None:

                test = selected_house.get_piece().get_type()
                if test == PAWN:
                    selected_house.get_piece().toggle_first_move()

                candidate_house.set_piece(selected_house.get_piece())
                selected_house.set_piece(None)
                board.switch_turn()

        # lógica de alteração da peça selecionada
        board.unselect_selected_house()
        return

    # seleciona a casa clicada
    selected_house = board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
        int(pygame.mouse.get_pos()[1] / (6.25 * 8))
    ]

    # verifica se há uma peça na casa
    
    if not selected_house.get_piece() is None:
        selected_piece = selected_house.get_piece()
        if selected_piece.get_color() == board.get_turn():
            possible_moves = selected_piece.get_possible_moves(board)

            for possible_move in possible_moves:
                board.houses[possible_move[0]][possible_move[1]].set_is_high_light(True)

            selected_piece.set_selected(True)
            


def restart_button_click_manager(mouse, screen):
    return (mouse.get_pos()[0] >= screen.get_width() / 4 and mouse.get_pos()[
        0] <= screen.get_width() / 4 + 200 and
            mouse.get_pos()[1] >= 440 and mouse.get_pos()[
                1] <= 440 + 25)


if __name__ == "__main__":
    main()

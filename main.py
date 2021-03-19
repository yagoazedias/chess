import pygame
from models.board import Board
from constants.types import PAWN, ROOK


def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption('Xadrez')
    pygame.display.flip()
    clock = pygame.time.Clock()

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                movement_manager(board)

        pygame.display.update()
        clock.tick(60)
        board.draw(screen)


def movement_manager(board):
    board.clean_high_ligths()
    selected_house = board.get_selected_house()

    if selected_house:

        candidate_house = board.houses[int(pygame.mouse.get_pos()[0] / (12.5 * 8))][
            int(pygame.mouse.get_pos()[1] / (12.5 * 8))]

        # lógica de movimentação e troca de casa da peça
        if candidate_house.get_position() \
                in selected_house.get_piece().get_possible_moves(board):

            # lógica de movimentação sem capitura (troca 'candidate_house' por 'selected_house' e o ultimo é anulado)
            if candidate_house.get_piece() is None:

                test = selected_house.get_piece().get_type()
                if test == PAWN:
                    selected_house.get_piece().toggle_first_move()

                candidate_house.set_piece(selected_house.get_piece())
                selected_house.set_piece(None)

        # lógica de alteração da peça selecionada
        board.unselect_selected_house()
        return

    # seleciona a casa clicada
    selected_house = board.houses[int(pygame.mouse.get_pos()[0] / (12.5 * 8))][
               int(pygame.mouse.get_pos()[1] / (12.5 * 8))]

    # verifica se há uma peça na casa
    if not selected_house.get_piece() is None:
        selected_piece = selected_house.get_piece()
        possible_moves = selected_piece.get_possible_moves(board)

        for possible_move in possible_moves:
            board.houses[possible_move[0]][possible_move[1]].set_is_high_light(True)

        selected_piece.set_selected(True)




if __name__ == "__main__":
    main()

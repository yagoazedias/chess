import pygame
from models.board import Board


def main():
    pygame.init()
    screen = pygame.display.set_mode([400, 400])
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
                board.clean_high_ligths()
                if not board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
                           int(pygame.mouse.get_pos()[1] / (6.25 * 8))].get_piece() is None:
                    possible_moves = board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
                        int(pygame.mouse.get_pos()[1] / (6.25 * 8))].get_piece().get_possible_moves(board)
                    for possible_move in possible_moves:
                        board.houses[possible_move[0]][possible_move[1]].set_is_high_ligth(True)

        pygame.display.update()
        clock.tick(60)
        board.draw(screen)


if __name__ == "__main__":
    main()

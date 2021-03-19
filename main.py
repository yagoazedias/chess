import pygame
from models.board import Board

pygame.init()


def prepare_player_turn_indicator(board, screen, font, x, y):
    text = "Vez das peças "
    text += "bracas" if board.turn == 0 else "pretas"
    indicator = font.render(text, True, (255, 255, 255))

    screen_width = screen.get_width() / 2
    text_width = indicator.get_width() / 2
    x = screen_width - text_width
    print(x)

    screen.blit(indicator, (x, y))


def main():
    # pygame.init()
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    textXPossition = 100
    textYPossition = 410

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.clean_high_ligths()
                if (
                    not board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
                        int(pygame.mouse.get_pos()[1] / (6.25 * 8))
                    ].get_piece()
                    is None
                ):
                    possible_moves = (
                        board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
                            int(pygame.mouse.get_pos()[1] / (6.25 * 8))
                        ]
                        .get_piece()
                        .get_possible_moves(board)
                    )
                    for possible_move in possible_moves:
                        board.houses[possible_move[0]][
                            possible_move[1]
                        ].set_is_high_ligth(True)

        prepare_player_turn_indicator(
            board, screen, text_font, textXPossition, textYPossition
        )
        pygame.display.update()
        clock.tick(60)
        board.draw(screen)


if __name__ == "__main__":
    main()

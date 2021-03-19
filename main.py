import pygame
from models.board import Board

pygame.init()


def prepare_player_turn_indicator(board, screen, font, x, y):
    text = "Vez das peças "
    text += "brancas" if board.turn == 0 else "pretas"
    indicator = font.render(text, True, (255, 255, 255))

    screen_width = screen.get_width() / 2
    text_width = indicator.get_width() / 2
    x = screen_width - text_width

    screen.blit(indicator, (x, y))


def draw_button(screen, text, height, width, x, y):
    text_font = pygame.font.Font(pygame.font.get_default_font(), int(height * 0.8))
    pygame.draw.rect(screen, (210, 210, 210), (x, y, width, height), 0, 3, 3, 3, 3)
    textButton = text_font.render(text, True, (0, 0, 0))
    screen.blit(textButton, (x + ((width - textButton.get_width()) / 2), y + height * 0.2))


def main():
    # pygame.init()
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()
    buttonTextStart = "Iniciar/Abandonar"

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.clean_high_ligths()
                if (pygame.mouse.get_pos()[1] <= 400 and
                        (not board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
                                int(pygame.mouse.get_pos()[1] / (6.25 * 8))
                            ].get_piece()
                            is None)
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
                elif (pygame.mouse.get_pos()[0] >= screen.get_width() / 4 and pygame.mouse.get_pos()[
                    0] <= screen.get_width() / 4 + 200 and
                      pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[
                          1] <= 440 + 25):
                    print("cliquei no botão")

        prepare_player_turn_indicator(
            board, screen, text_font, 100, 410
        )

        draw_button(screen, buttonTextStart, 25, 200, screen.get_width() / 4, 440)

        pygame.display.update()
        clock.tick(60)
        board.draw(screen)


if __name__ == "__main__":
    main()

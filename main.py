import pygame
from models.board import Board


def main():
    pygame.init()
    screen = pygame.display.set_mode([700, 700])
    pygame.display.set_caption('Olá mundo')
    screen.fill([0, 0, 0])
    pygame.display.flip()

    board = Board()
    board.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()

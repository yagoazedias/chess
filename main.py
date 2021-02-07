import time

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption('Olá mundo')
    screen.fill([0, 0, 0])
    pygame.display.flip()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

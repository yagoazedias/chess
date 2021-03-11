import pygame
from models.board import Board

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
                    
        pygame.display.update()
        clock.tick(60)
        board.draw(screen)


if __name__ == "__main__":
    main()

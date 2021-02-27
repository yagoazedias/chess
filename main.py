import time
import pygame

from piece import Piece

from models.board import Board


def main():
    pygame.init()
    screen = pygame.display.set_mode([700, 700])
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption('Olá mundo')
    screen.fill(pygame.Color("white"))
    pygame.display.flip()

    board = Board()

    board.houses[0][0].set_piece(Piece(0, 0, "black", 1))
    board.houses[0][1].set_piece(Piece(0, 1, "black", 2))
    board.houses[0][2].set_piece(Piece(0, 2, "black", 3))
    board.houses[0][3].set_piece(Piece(0, 3, "black", 4))
    board.houses[0][4].set_piece(Piece(0, 4, "black", 5))
    board.houses[0][5].set_piece(Piece(0, 5, "black", 3))
    board.houses[0][6].set_piece(Piece(0, 6, "black", 2))
    board.houses[0][7].set_piece(Piece(0, 7, "black", 1))
    
    board.houses[1][0].set_piece(Piece(1, 0, "black", 0))
    board.houses[1][1].set_piece(Piece(1, 1, "black", 0))
    board.houses[1][2].set_piece(Piece(1, 2, "black", 0))
    board.houses[1][3].set_piece(Piece(1, 3, "black", 0))
    board.houses[1][4].set_piece(Piece(1, 4, "black", 0))
    board.houses[1][5].set_piece(Piece(1, 5, "black", 0))
    board.houses[1][6].set_piece(Piece(1, 6, "black", 0))
    board.houses[1][7].set_piece(Piece(1, 7, "black", 0))
    
    board.houses[7][0].set_piece(Piece(7, 0, "white", 1))
    board.houses[7][1].set_piece(Piece(7, 1, "white", 2))
    board.houses[7][2].set_piece(Piece(7, 2, "white", 3))
    board.houses[7][3].set_piece(Piece(7, 3, "white", 4))
    board.houses[7][4].set_piece(Piece(7, 4, "white", 5))
    board.houses[7][5].set_piece(Piece(7, 5, "white", 3))
    board.houses[7][6].set_piece(Piece(7, 6, "white", 2))
    board.houses[7][7].set_piece(Piece(7, 7, "white", 1))
    
    board.houses[6][0].set_piece(Piece(6, 0, "white", 0))
    board.houses[6][1].set_piece(Piece(6, 1, "white", 0))
    board.houses[6][2].set_piece(Piece(6, 2, "white", 0))
    board.houses[6][3].set_piece(Piece(6, 3, "white", 0))
    board.houses[6][4].set_piece(Piece(6, 4, "white", 0))
    board.houses[6][5].set_piece(Piece(6, 5, "white", 0))
    board.houses[6][6].set_piece(Piece(6, 6, "white", 0))
    board.houses[6][7].set_piece(Piece(6, 7, "white", 0))
    
    
    board.draw(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()

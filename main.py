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
    board.draw(screen)

    piece00 = Piece(0, 0, "black", 1)
    piece01 = Piece(0, 1, "black", 2)
    piece10 = Piece(1, 0, "black", 0)
    piece11 = Piece(1, 1, "black", 0)
    piece60 = Piece(6, 0, "white", 0)
    piece61 = Piece(6, 1, "white", 0)
    piece70 = Piece(7, 0, "white", 1)
    piece71 = Piece(7, 1, "white", 2)

    piece00.draw(screen, "black")
    piece01.draw(screen, "black")
    piece10.draw(screen, "black")
    piece11.draw(screen, "black")
    piece60.draw(screen, "white")
    piece61.draw(screen, "white")
    piece70.draw(screen, "white")
    piece71.draw(screen, "white")
    print(piece00.get_possition())
    print(piece00.get_color())
    print(piece00.is_selected())


    # board = [[0 for x in range(8)] for _ in range(8)]

    # board[0][0] = Piece(0, 0, "black", 1)
    # board[0][1] = Piece(0, 1, "black", 2)
    # board[0][2] = Piece(0, 2, "black", 3)
    # board[0][3] = Piece(0, 3, "black", 4)
    # board[0][4] = Piece(0, 4, "black", 5)
    # board[0][5] = Piece(0, 5, "black", 3)
    # board[0][6] = Piece(0, 6, "black", 2)
    # board[0][7] = Piece(0, 7, "black", 1)
    #
    # board[1][0] = Piece(1, 0, "black", 0)
    # board[1][1] = Piece(1, 1, "black", 0)
    # board[1][2] = Piece(1, 2, "black", 0)
    # board[1][3] = Piece(1, 3, "black", 0)
    # board[1][4] = Piece(1, 4, "black", 0)
    # board[1][5] = Piece(1, 5, "black", 0)
    # board[1][6] = Piece(1, 6, "black", 0)
    # board[1][7] = Piece(1, 7, "black", 0)
    #
    # board[7][0] = Piece(7, 0, "white", 1)
    # board[7][1] = Piece(7, 1, "white", 2)
    # board[7][2] = Piece(7, 2, "white", 3)
    # board[7][3] = Piece(7, 3, "white", 4)
    # board[7][4] = Piece(7, 4, "white", 5)
    # board[7][5] = Piece(7, 5, "white", 3)
    # board[7][6] = Piece(7, 6, "white", 2)
    # board[7][7] = Piece(7, 7, "white", 1)
    #
    # board[6][0] = Piece(6, 0, "white", 0)
    # board[6][1] = Piece(6, 1, "white", 0)
    # board[6][2] = Piece(6, 2, "white", 0)
    # board[6][3] = Piece(6, 3, "white", 0)
    # board[6][4] = Piece(6, 4, "white", 0)
    # board[6][5] = Piece(6, 5, "white", 0)
    # board[6][6] = Piece(6, 6, "white", 0)
    # board[6][7] = Piece(6, 7, "white", 0)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()

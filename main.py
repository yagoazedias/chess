import pygame

from models.piece import Piece
from models.board import Board

from constants import images


def main():
    # board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    #          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-', '-', '-', '-'],
    #          ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    #          ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
    #
    # teste = Pawn(1, 1, "black", 0)

    pygame.init()
    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption('Xadrez')
    pygame.display.flip()

    board = Board()

    board.houses[0][0].set_piece(Piece(0, 0, "black", images.black_rook))
    board.houses[1][0].set_piece(Piece(0, 1, "black", images.black_horse))
    board.houses[2][0].set_piece(Piece(0, 2, "black", images.black_bishop))
    board.houses[3][0].set_piece(Piece(0, 3, "black", images.black_queen))
    board.houses[4][0].set_piece(Piece(0, 4, "black", images.black_king))
    board.houses[5][0].set_piece(Piece(0, 5, "black", images.black_bishop))
    board.houses[6][0].set_piece(Piece(0, 6, "black", images.black_horse))
    board.houses[7][0].set_piece(Piece(0, 7, "black", images.black_rook))

    board.houses[0][1].set_piece(Piece(1, 0, "black", images.black_pawn))
    board.houses[1][1].set_piece(Piece(1, 1, "black", images.black_pawn))
    board.houses[2][1].set_piece(Piece(1, 2, "black", images.black_pawn))
    board.houses[3][1].set_piece(Piece(1, 3, "black", images.black_pawn))
    board.houses[4][1].set_piece(Piece(1, 4, "black", images.black_pawn))
    board.houses[5][1].set_piece(Piece(1, 5, "black", images.black_pawn))
    board.houses[6][1].set_piece(Piece(1, 6, "black", images.black_pawn))
    board.houses[7][1].set_piece(Piece(1, 7, "black", images.black_pawn))

    board.houses[0][7].set_piece(Piece(7, 0, "white", images.white_rook))
    board.houses[1][7].set_piece(Piece(7, 1, "white", images.white_horse))
    board.houses[2][7].set_piece(Piece(7, 2, "white", images.white_bishop))
    board.houses[3][7].set_piece(Piece(7, 3, "white", images.white_queen))
    board.houses[4][7].set_piece(Piece(7, 4, "white", images.white_king))
    board.houses[5][7].set_piece(Piece(7, 5, "white", images.white_bishop))
    board.houses[6][7].set_piece(Piece(7, 6, "white", images.white_horse))
    board.houses[7][7].set_piece(Piece(7, 7, "white", images.white_rook))

    board.houses[0][6].set_piece(Piece(6, 0, "white", images.white_pawn))
    board.houses[1][6].set_piece(Piece(6, 1, "white", images.white_pawn))
    board.houses[2][6].set_piece(Piece(6, 2, "white", images.white_pawn))
    board.houses[3][6].set_piece(Piece(6, 3, "white", images.white_pawn))
    board.houses[4][6].set_piece(Piece(6, 4, "white", images.white_pawn))
    board.houses[5][6].set_piece(Piece(6, 5, "white", images.white_pawn))
    board.houses[6][6].set_piece(Piece(6, 6, "white", images.white_pawn))
    board.houses[7][6].set_piece(Piece(6, 7, "white", images.white_pawn))

    board.draw(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()

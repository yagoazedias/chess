import pygame
from models.board import Board
from models.ia import Ia
from constants.colors import *

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 20)

    board = Board()
    ia = Ia(board)
    ia_on = True
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if board.get_turn() == BLACK and ia_on:
                ia.move()
            if event.type == pygame.MOUSEBUTTONDOWN:                    
                if pygame.mouse.get_pos()[1] <= 400:
                    clicked_house = get_clicked_house(board)
                    board.movement_manager(clicked_house,None)
                elif restart_button_click_manager(pygame.mouse, screen):
                    board.prepare_board()

        pygame.display.update()
        clock.tick(60)
        board.draw(screen,text_font)

def get_clicked_house(board):
    return board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
        int(pygame.mouse.get_pos()[1] / (6.25 * 8))]

def restart_button_click_manager(mouse, screen):
    return (mouse.get_pos()[0] >= screen.get_width() / 4 and mouse.get_pos()[
        0] <= screen.get_width() / 4 + 200 and
            mouse.get_pos()[1] >= 440 and mouse.get_pos()[
                1] <= 440 + 25)

if __name__ == "__main__":
    main()

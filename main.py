import pygame
from models.match import Match
from models.ia import Ia
from constants.colors import *

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 500])
    pygame.display.set_caption("Xadrez")
    pygame.display.flip()
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 18)

    match = Match()
    ia = Ia(match)
    ia_on = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if match.get_turn() == BLACK and ia_on:
                ia.move()
            if event.type == pygame.MOUSEBUTTONDOWN:                    
                if pygame.mouse.get_pos()[1] <= 400:
                    clicked_house = get_clicked_house(match)
                    match.movement_manager(clicked_house,None)
                elif button_click_manager(pygame.mouse, screen):
                    match.button_manager()

        pygame.display.update()
        clock.tick(60)
        match.draw(screen,text_font)

def get_clicked_house(match):
    return match.board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
        int(pygame.mouse.get_pos()[1] / (6.25 * 8))]

def button_click_manager(mouse, screen):
    return (mouse.get_pos()[0] >= screen.get_width() / 4 and mouse.get_pos()[
        0] <= screen.get_width() / 4 + 200 and
            mouse.get_pos()[1] >= 440 and mouse.get_pos()[
                1] <= 440 + 25)

if __name__ == "__main__":
    main()

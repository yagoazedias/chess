import pygame
from models.match import Match
from models.ia import Ia
from constants.colors import *

pygame.init()

def main():
    screen = pygame.display.set_mode([400, 400])
    pygame.display.set_caption("Xadrez")
    
    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font(pygame.font.get_default_font(), 18)

    match = Match()
    ia = Ia(match)
    
    running = True
    ia_on = True
    
    while running:                
        match.is_checkmate = match.checkmate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if match.get_turn() == BLACK and ia_on and not match.is_checkmate:
                ia.move()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if match.choice:                   
                    if pygame.mouse.get_pos()[1] <= 400:
                        clicked_house = get_clicked_house(match)
                        match.movement_manager(clicked_house,None)
                    elif button_click_manager(screen):
                        if not match.checked:
                            screen = pygame.display.set_mode([400, 400])
                        match.button_manager()
                        
                else:
                    if pygame.mouse.get_pos()[0] >= 45 and pygame.mouse.get_pos()[0] <= 125 and pygame.mouse.get_pos()[1] >= 182 and pygame.mouse.get_pos()[1] <= 210:
                        ia_on = False
                    elif pygame.mouse.get_pos()[0] >= 158 and pygame.mouse.get_pos()[0] <= 242 and pygame.mouse.get_pos()[1] >= 182 and pygame.mouse.get_pos()[1] <= 210:
                        ia_on = True
                    match.choice = True
                    screen = pygame.display.set_mode([400, 500])

        pygame.display.update()
        clock.tick(60)
        match.draw(screen,text_font)

def get_clicked_house(match):
    return match.board.houses[int(pygame.mouse.get_pos()[0] / (6.25 * 8))][
        int(pygame.mouse.get_pos()[1] / (6.25 * 8))]

def button_click_manager(screen):
    return (pygame.mouse.get_pos()[0] >= screen.get_width() / 4 and pygame.mouse.get_pos()[
        0] <= screen.get_width() / 4 + 200 and
            pygame.mouse.get_pos()[1] >= 440 and pygame.mouse.get_pos()[
                1] <= 440 + 25)

if __name__ == "__main__":
    main()

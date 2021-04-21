import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame
import ctypes
from models.match import Match
from models.ia import Ia
from constants.colors import *
from constants.screens import Screens

def main():
    pygame.init()
    screen = pygame.display.set_mode([400, 400])
    pygame.display.set_caption("Xadrez")

    clock = pygame.time.Clock()

    # defining Text font
    text_font = pygame.font.Font("font/FreeSansBold.ttf", 18)

    match = Match()
    ia = Ia(match)

    running = True
    ia_on = True

    while running:
        match.is_checkmate = match.checkmate()

        for event in pygame.event.get():
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

            if event.type == pygame.QUIT:
                running = False
            if match.get_turn() == BLACK and ia_on and not match.is_checkmate and not match.get_is_stalemate():
                ia.move()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if match.choice:  # Match has already started
                    if mouse_y <= 400:
                        clicked_house = get_clicked_house(match)
                        match.movement_manager(clicked_house, None)
                    elif button_click_manager(screen):
                        if not match.checked:
                            screen = pygame.display.set_mode([400, 400])
                        match.button_manager()

                else:
                    if has_clicked_on_p_vs_p(mouse_x, mouse_y):
                        start_match(match, screen)
                        ia_on = False
                    elif has_clicked_on_ia(mouse_x, mouse_y):
                        start_match(match, screen)
                        ia_on = True
                    elif has_clicked_on_credits(mouse_x, mouse_y):
                        show_credits_screen(match)
                    elif has_clicked_on_go_to_menu(mouse_x, mouse_y):
                        show_menu_screen(match)

        pygame.display.update()
        clock.tick(60)
        match.draw(screen, text_font)


def start_match(match, screen):
    if match.screen_name == Screens.MENU:
        match.screen_name = Screens.GAME
        match.choice = True
        screen = pygame.display.set_mode([400, 500])


def show_menu_screen(match):
    if match.screen_name != Screens.MENU:
        match.screen_name = Screens.MENU


def show_credits_screen(match):
    if match.screen_name != Screens.CREDITS:
        match.screen_name = Screens.CREDITS


def has_clicked_on_go_to_menu(x, y):
    return 300 <= x <= 360 and 320 <= y <= 360


def has_clicked_on_p_vs_p(x, y):
    return 45 <= x <= 125 and 182 <= y <= 210


def has_clicked_on_ia(x, y):
    return 158 <= x <= 242 and 182 <= y <= 210


def has_clicked_on_credits(x, y):
    return 275 <= x <= 350 and 182 <= y <= 210


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

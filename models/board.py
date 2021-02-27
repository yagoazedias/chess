from models.house import House

BOARD_BLACK = 36, 170, 173
BOARD_WHITE = 148, 233, 235

class Board:

    def __init__(self):
        self.turn = 0
        self.winner = None
        self.houses = [[0 for _ in range(8)] for __ in range(8)]
        self.set_up()

    def draw(self, display):
        for row in range(0, 8):
            for col in range(0, 8):
                self.houses[row][col].draw(display)

    def set_up(self):
        for row in range(0, 8):
            color_index = row % 2
            for col in range(0, 8):
                color = BOARD_WHITE if color_index == 0 else BOARD_BLACK
                self.houses[row][col] = House(row, col, color)
                color_index = (color_index + 1) % 2

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

    def move_piece(self):
        print("move_piece")

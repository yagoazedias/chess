class Board:

    def __init__(self):
        self.turn = 0
        self.winner = None
        self.houses = None

    def draw(self):
        print("draw")

    def set_up(self):
        print("set_up")

    def get_danger_moves(self):
        print("get_danger_moves")

    def is_checked(self):
        print("is_checked")
        return False

    def move_piece(self):
        print("move_piece")
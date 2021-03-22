from models.board import Board
from constants.types import PAWN, ROOK
from constants.colors import *
from random import choices
import time

class Ia:
  def __init__(self, board):
    self.board = board

  def move(self):
    
    if self.board.get_turn() == BLACK:
      possible_moves = []
      selected_house = None
      candidate_house = None
      
      while True:
        position = choices(self.search_blacks())[0]
        selected_house = self.board.get_house(position)
        
        possible_moves = selected_house.get_piece().get_possible_moves(self.board)
        if len(possible_moves) > 0:
          break
        
      move = choices(possible_moves)[0]
      
      candidate_house = self.board.get_house(move)
      
      test = selected_house.get_piece().get_type()
      if test == PAWN:
          selected_house.get_piece().toggle_first_move()

      candidate_house.set_piece(selected_house.get_piece())
      selected_house.set_piece(None)
      
      self.board.switch_turn()
      
  def search_blacks(self):
    positions = []
    for col in range(0, 8):
      for row in range(0, 8):
        if self.board.houses[col][row].get_piece() is not None:
          if self.board.houses[col][row].get_piece().get_color() == BLACK:
            positions.append((col,row))
    return positions

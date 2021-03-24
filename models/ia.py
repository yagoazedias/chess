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
      
      positions = self.select_piece_and_desired_house()
      
      selected_house = positions[0]
      desired_house = positions[1]    
      
      self.board.movement_manager(selected_house, desired_house)
      
  def select_piece_and_desired_house(self):
    position = (-1,-1)
    possible_moves = []
    selected_piece = None
    while True:
      position = choices(self.search_blacks())[0]
      selected_piece = self.board.get_house(position)
      
      possible_moves = selected_piece.get_piece().get_possible_moves(self.board)
      if len(possible_moves) > 0:
        break
        
    move = choices(possible_moves)[0]
    desired_house = self.board.get_house(move)
    return selected_piece, desired_house
      
  def search_blacks(self):
    positions = []
    for col in range(0, 8):
      for row in range(0, 8):
        if self.board.houses[col][row].get_piece() is not None:
          if self.board.houses[col][row].get_piece().get_color() == BLACK:
            positions.append((col,row))
    return positions

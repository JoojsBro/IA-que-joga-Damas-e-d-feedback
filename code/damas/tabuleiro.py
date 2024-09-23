import pygame
from .constantes import BLACK, ROWS, PURPLE, SQUARE_SIZE

class Tabuleiro:
   def __init__(self,):
      self.tabuleiro = []
      self.selected_piece = None
      self.purple_left = self.white_left = 12
      self.purple_kings = self.white_kings = 0

   def draw_squares(self, win):
      win.fill(BLACK)
      for row in range(ROWS):
         for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(win, PURPLE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

   def create_board(self):
      pass
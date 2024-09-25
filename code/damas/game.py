import pygame
from .constantes import PURPLE, WHITE
from .tabuleiro import Tabuleiro
from .peca import Peca

class Game:
   def __init__(self, win):
      self._init()
      self.win = win

   def update(self):
      self.tabuleiro.draw(self.win)
      pygame.display.update()

   def _init(self):
      self.selected = None
      self.tabuleiro = Tabuleiro()
      self.turn = PURPLE
      self.valid_moves = {}

   def reset(self):
      self._init()

   def select(self, row, col):
      if self.selected:
         result = self._move(row, col)
         if not result:
            self.selected = None
            self.select(row, col)
      else:
         peca = self.tabuleiro.get_peca(row, col)
         if peca != 0 and self.peca.color == self.turn:
            self.selected = peca
            self.valid_moves = self.tabuleiro.get_valid_moves(peca)
            return True
      
      return False

   def _move(self, row, col):
      peca = self.tabuleiro.get_peca(row, col)
      if self.selected and peca == 0 and (row, col) in self.valid_moves:
         self.tabuleiro.move(self.selected, row, col)
      else:
         return False
      
      return True
   
   def change_turn(self):
      if self.turn == PURPLE:
         self.turn = WHITE
      else:
         self.turn = PURPLE
import pygame
from .tabuleiro import Tabuleiro
from .constantes import PURPLE, WHITE, GREEN, SQUARE_SIZE

class Game:
   def __init__(self, win):
      self._init()
      self.win = win

   def update(self):
      self.tabuleiro.draw(self.win)
      self.draw_valid_moves(self.valid_moves)
      pygame.display.update()

   def _init(self):
      self.selected = None
      self.tabuleiro = Tabuleiro()
      self.turn = PURPLE
      self.valid_moves = {}

   def winner(self):
      return self.tabuleiro.winner()

   def reset(self):
      self._init()

   def select(self, row, col):
      if self.selected:
         result = self._move(row, col)
         if not result:
            self.selected = None
            self.select(row, col)
       
      peca = self.tabuleiro.get_peca(row, col)
      if peca != 0 and peca.color == self.turn:
         self.selected = peca
         self.valid_moves = self.tabuleiro.get_valid_moves(peca)
         return True
      
      return False

   def _move(self, row, col):
      peca = self.tabuleiro.get_peca(row, col)
      if self.selected and peca == 0 and (row, col) in self.valid_moves:
         self.tabuleiro.move(self.selected, row, col)
         skipped = self.valid_moves[(row, col)]
         if skipped:
            self.tabuleiro.remove(skipped)
         self.change_turn()
      else:
         return False
      
      return True
   
   def draw_valid_moves(self, moves):
      for move in moves:
         row, col = move
         pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
   
   def change_turn(self):
      self.valid_moves = {}
      if self.turn == PURPLE:
         self.turn = WHITE
      else:
         self.turn = PURPLE
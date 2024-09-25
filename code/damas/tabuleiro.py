import pygame
from .peca import Peca
from .constantes import BLACK, ROWS, PURPLE, SQUARE_SIZE, COLS, WHITE

class Tabuleiro:
   def __init__(self,):
      self.tabuleiro = []
      self.purple_left = self.white_left = 12
      self.purple_kings = self.white_kings = 0
      self.create_board()

   def draw_squares(self, win):
      win.fill(BLACK)
      for row in range(ROWS):
         for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(win, PURPLE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

   def move(self, peca, row, col):
      self.tabuleiro[peca.row] [peca.col], self.tabuleiro[row] [col] = self.tabuleiro[row][col], self.tabuleiro[peca.row][peca.col]
      peca.move(row, col)

      if row == ROWS or row == 0:
         peca.make_king()
         if peca.color == WHITE:
            self.white_kings += 1
         else:
            self.purple_kings += 1

   def get_peca(self, row, col):
      return self.tabuleiro[row][col]

   def create_board(self):
      for row in range(ROWS):
         self.tabuleiro.append([])
         for col in range(COLS):
            if col % 2 == ((row+ 1) % 2):
               if row < 3:
                  self.tabuleiro[row].append(Peca(row, col, WHITE))
               elif row > 4:
                  self.tabuleiro[row].append(Peca(row,col,PURPLE))
               else:
                  self.tabuleiro[row].append(0)
            else:
               self.tabuleiro[row].append(0)

   def draw(self, win):
      self.draw_squares(win)
      for row in range(ROWS):
         for col in range(COLS):
            peca = self.tabuleiro[row][col]
            if peca != 0:
               peca.draw(win)

#TODO parou no terceiro vídeo no tempo 16:49
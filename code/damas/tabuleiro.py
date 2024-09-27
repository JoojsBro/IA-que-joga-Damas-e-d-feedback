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

   def get_valid_moves(self, peca):
      moves = {}
      left = peca.col -1
      right = peca.col +1
      row = peca.row

      if peca.color == PURPLE or peca.king:
         moves.update(self._traverse_left(row -1, max(row -3, -1), -1, peca.color, left))
         moves.update(self._traverse_left(row -1, max(row -3, -1), -1, peca.color, right))

      if peca.color == WHITE or peca.king:
         moves.update(self._traverse_left(row +1, max(row +3, +1), 1, peca.color, left))
         moves.update(self._traverse_left(row +1, max(row +3, +1), 1, peca.color, right))

      return moves

   def _traverse_left(self, start, stop, step, color, left, skipped=[]):
      moves = {}
      last = []
      for r in range(start, stop, step):
         if left < 0:
            break
         
         current = self.tabuleiro[r][left]
         if current == 0:
            if skipped and not last:
               break
            elif skipped:
               moves[(r, left)] = last + skipped
            else:
               moves[(r, left)] = last

            if last:
               if step == -1:
                  row = max(r-3, 0)
               else:
                  row = min(r+3, ROWS)

               moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
               moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
               break

         elif current.color == color:
            break
         else:
            last = [current]

         left -=1
      
      return moves


   def _traverse_right(self, start, stop, step, color, right, skipped=[]):
      moves = {}
      last = []
      for r in range(start, stop, step):
         if right >= COLS:
            break
         
         current = self.tabuleiro[r][right]
         if current == 0:
            if skipped and not last:
               break
            elif skipped:
               moves[(r, right)] = last + skipped
            else:
               moves[(r, right)] = last

            if last:
               if step == -1:
                  row = max(r-3, 0)
               else:
                  row = min(r+3, ROWS)

               moves.update(self._traverse_left(r+step, row, step, color, right+1, skipped=last))
               moves.update(self._traverse_right(r+step, row, step, color, right-1, skipped=last))
               break

         elif current.color == color:
            break
         else:
            last = [current]

         right +=1

      return moves
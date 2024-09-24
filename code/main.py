import pygame
from damas.constantes import WIDTH, HEIGHT, SQUARE_SIZE
from damas.tabuleiro import Tabuleiro

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')

def get_row_col_from_mouse(pos):
   x, y = pos
   row = y // SQUARE_SIZE
   col = x // SQUARE_SIZE
   return row, col

def main():
   run = True
   clock = pygame.time.Clock()
   tabuleiro = Tabuleiro()
   peca = tabuleiro.get_peca(0,1)

   while run:
      clock.tick(FPS)
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

         if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            peca = tabuleiro.get_peca(row, col)
            tabuleiro.move(peca, 4, 3)

      tabuleiro.draw(WIN)
      pygame.display.update()

   pygame.quit()

main()
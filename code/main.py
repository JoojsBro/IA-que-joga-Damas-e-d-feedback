import pygame
from damas.constantes import WIDTH, HEIGHT, SQUARE_SIZE
from damas.tabuleiro import Tabuleiro
from damas.game import Game

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
   game = Game(WIN)


   while run:
      clock.tick(FPS)
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

         if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            

      game.update()

   pygame.quit()

main()

#TODO parou em 45:35 no vídeo 3 do tutorial de montar o jogo
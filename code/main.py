import pygame
from damas.constantes import WIDTH, HEIGHT
from damas.tabuleiro import Tabuleiro

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Damas')

def main():
   run = True
   clock = pygame.time.Clock()
   tabuleiro = Tabuleiro()

   while run:
      clock.tick(FPS)
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False

         if event.type == pygame.MOUSEBUTTONUP:
            pass
      tabuleiro.draw_squares(WIN)
      pygame.display.update()

   pygame.quit()

main()
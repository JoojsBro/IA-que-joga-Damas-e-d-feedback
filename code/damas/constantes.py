import pygame

WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#RGB
WHITE = (255,255,255)
PURPLE = (110,60,190)
GREEN = (0,184,82)
BLACK = (0,0,0)
BLUE = (0, 127, 255)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
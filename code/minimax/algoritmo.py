from copy import deepcopy
import pygame

WHITE = (255,255,255)
PURPLE = (110,60,190)

def minimax(position, depth, max_player, game):
   if depth == 0 or position.winner() != None:
      return position.evaluate(), position
   
   if max_player:
      maxEval = float('-inf')
      best_move = None
      for move in get_all_moves(position, WHITE, game):
         evaluation = minimax(move, depth-1, False, game)[0]
         maxEval = max(maxEval, evaluation)
         if maxEval == evaluation:
            best_move = move

      return maxEval, best_move

   else:
      minEval = float('inf')
      best_move = None
      for move in get_all_moves(position, PURPLE, game):
         evaluation = minimax(move, depth-1, True, game)[0]
         minEval = min(minEval, evaluation)
         if minEval == evaluation:
            best_move = move

      return minEval, best_move

def simulate_move(peca, move, tabuleiro, game, skip):
   tabuleiro.move(peca, move[0], move[1])
   if skip:
      tabuleiro.remove(skip)

   return tabuleiro

def get_all_moves(tabuleiro, color, game):
   moves = []

   for peca in tabuleiro.get_all_pecas(color):
      valid_moves = tabuleiro.get_valid_moves(peca)
      for move, skip in valid_moves.items():
         temp_tabuleiro = deepcopy(tabuleiro)
         temp_peca = temp_tabuleiro.get_peca(peca.row, peca.col)
         new_tabuleiro = simulate_move(temp_peca, move, temp_tabuleiro, game, skip)
         moves.append(new_tabuleiro)

   return moves

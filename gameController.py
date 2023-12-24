from menu import Menu
from board import Board
from mastermind import Mastermind

class GameController:
     def __init__(self,pygame, screen):
          self._pygame = pygame
          self._screen = screen
          self._menu = Menu(pygame, screen)
          
          self.screen = self._menu

     def message(self, command):
          if command == "start":
               self._mastermind = Mastermind(self._menu.slots, self._menu.colours, self._menu.guesses)
               self.board = Board(self._mastermind, self._pygame, self._screen)
               self.screen = self.board
          elif command == "exitboard":
               self.screen = self._menu
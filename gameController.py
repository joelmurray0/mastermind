from menu import Menu
from board import Board
from mastermind import Mastermind

class GameController:
     def __init__(self,pygame, screen):
          self._menu = Menu(pygame, screen)
          self._board = Board(pygame, screen)
          self._mastermind = Mastermind(4,4,12)
          self.screen = self._menu
     
     def message(self, command):
          if command == "start":
               self.screen = self._board
          elif command == "enter":
               self.screen = self._menu
from menu import Menu
from board import Board
from load import Load
from mastermind import Mastermind

class GameController:
     def __init__(self,pygame, screen):
          self._pygame = pygame
          self._screen = screen
          self._menu = Menu(pygame, screen)
          self._load = Load("save.txt")
          self.screen = self._menu

     def message(self, command):
          if command == "start":
               self._mastermind = Mastermind(self._menu.slots, self._menu.colours, self._menu.guesses, self._menu.duplicate_mode)
               self.board = Board(self._mastermind, self._pygame, self._screen)
               self.screen = self.board
          elif command == "exitboard":
               self.screen = self._menu
          elif command == "rules":
               self.screen = self._rules
          elif command == "restore":
               self._mastermind = self._load.load_onclick()
               self.board = Board(self._mastermind, self._pygame, self._screen)
               self.screen = self.board
from menu import Menu
from board import Board
from rules import Rules
from load import Load
from mastermind import Mastermind
import pickle

class GameController:
     def __init__(self,pygame, screen):
          self._pygame = pygame
          self._screen = screen
          self._menu = Menu(pygame, screen)
          self._load = Load(pygame, screen)
          #self._rules = Rules(pygame, screen)
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
               self._mastermind = pickle.load(open("save.txt", "rb"))
               self.board = Board(self._mastermind, self._pygame, self._screen)
               self.screen = self.board
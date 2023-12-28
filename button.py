class Button:
     def __init__(self, x, y, btn_colour, pygame):
          self._pygame = pygame
          self.btn_colour = btn_colour
          self._center = (x, y)
     
     def onclick(self, game_controller):
          print("Loading...")
     
     def null(self, game_controller):
          pass
from button import Button
from pygame import Rect

class RectButton(Button):
     def __init__(self, x, y, colours, btn_width, btn_height, btn_colour, pygame):
          super().__init__(x, y, btn_colour, pygame)
          self._colours = colours
          self._btn_width = btn_width
          self._btn_height = btn_height
          self._rect = self.make_rect()

     def onhover(self):
          return [0]
     
     def make_rect(self):
          return Rect(self._center[0] - 0.5*self._btn_width, self._center[1] - 0.5*self._btn_height, self._btn_width, self._btn_height)
     
     def btn_draw(self, screen):
          self._pygame.draw.rect(screen, self.btn_colour, self._rect)
     
     def colour_shift(self, game_controller):
          if self.btn_colour == (128,128,128):
               index = -1
          else:
               index = self._colours.index(self.btn_colour)
          self.btn_colour = self._colours[(index + 1)%len(self._colours)]
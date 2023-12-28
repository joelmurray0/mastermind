from button import Button
from infoPanel import InfoPanel

class Screen:
     def __init__(self, screen):
          self._screen = screen
          self._btn_dict = {}
          self._circle_dict = {}
          self._text_dict = {}
          self._arrows_dict = {}
     
     def draw(self):
          for i in self._btn_dict:
               self._btn_dict[i].btn_draw(self._screen)
          for i in self._circle_dict:
               self._circle_dict[i].circle_draw(self._screen)
          for i in self._text_dict:
               self._text_dict[i].text_draw(self._screen)
          for i in self._arrows_dict:
               self._arrows_dict[i].btn_draw(self._screen)


     def on_mouse_down(self, pos, game_controller):
          clone_btn_dict = self._btn_dict.copy()
          for i in clone_btn_dict:
               if clone_btn_dict[i]._rect.collidepoint(pos):
                    clone_btn_dict[i].onclick(game_controller)

     def on_mouse_up(self, pos):
          self._arrows_dict = {}
          clone_btn_dict = self._btn_dict.copy()
          for i in clone_btn_dict:
               if clone_btn_dict[i]._rect.collidepoint(pos):
                    chr = clone_btn_dict[i].onhover()
                    if len(chr) == 2:
                         self._arrows_dict[">"] = chr[0]
                         self._arrows_dict["<"] = chr[1]

     def add_button(self, name, button):
          self._btn_dict[name] = button
     
     def text_box_write(self,font_size, message):
          return InfoPanel(400, 15, 800, 80, message, font_size, "arcadeclassic\ARCADECLASSIC.TTF", self._pygame)
from button import Button

class Screen:
     def __init__(self, screen):
          self._screen = screen
          self._btn_dict = {}
     
     def draw(self):
               for i in self._btn_dict:
                    self._btn_dict[i].btn_draw(self._screen)

     def on_mouse_down(self, pos, game_controller):
          for i in self._btn_dict:
               if self._btn_dict[i].rect.collidepoint(pos):
                    self._btn_dict[i].onclick(game_controller)

     def add_button(self, name, button):
          self._btn_dict[name] = button
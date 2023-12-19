from screen import Screen
from button import Button

class Board(Screen):
     def __init__(self, pygame, screen):
          super().__init__(screen)
          enter_btn = Button(400, 200, (0,128,128), "Go", 'freesansbold.ttf', 32, (255,255,255), pygame)
          enter_btn.onclick = self.enter_onclick
          self.add_button("start", enter_btn)
     
     def enter_onclick(self, game_controller):
          game_controller.message("enter")
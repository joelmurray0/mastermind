from screen import Screen
from button import Button

class Menu(Screen):
     def __init__(self, pygame, screen):
          super().__init__(screen)
          start_btn = Button(400, 200, (0,128,128), "Start", 'freesansbold.ttf', 32, (255,255,255), pygame)
          start_btn.onclick = self.start_onclick
          self.add_button("start", start_btn)
     
     def start_onclick(self, game_controller):
          game_controller.message("start")
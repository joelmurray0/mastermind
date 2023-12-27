from screen import Screen
from textBtn import TextButton
import pickle

class Load(Screen):
     def __init__(self, pygame, screen):
          super().__init__(screen)
          self._pygame = pygame
          self.save_number = 0

          exit_btn = TextButton(100, 50, (0,128,128), "Quit", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          exit_btn.onclick = self.exit_onclick
          self.add_button("exit", exit_btn)
     
     def save_file(self, filename):
          self.save_number += 1
          with open(filename,"r") as firstfile, open(f"{self.save_number}.txt","a") as secondfile: 
               for line in firstfile:
                         secondfile.write(line)
     
     def load_onclick(self, btn_num):
          return pickle.load(f"{btn_num}.txt")
     
     def exit_onclick(self, game_controller):
          game_controller.message("exitboard")
     

     
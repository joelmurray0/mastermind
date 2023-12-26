from screen import Screen
from textBtn import TextButton
from rectBtn import RectButton

def increment(lower, upper, current):
     output = 0
     if upper == current:
          output = lower
     else:
          output = current + 1
     return output

class Menu(Screen):
     def __init__(self, pygame, screen):
          super().__init__(screen)
          self._pygame = pygame
          self.slots = 4
          self.guesses = 10
          self.colours = 4
          self.duplicate_mode = False

          start_btn = TextButton(400, 100, (0,128,128), "Start", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          start_btn.onclick = self.start_onclick
          self.add_button("start", start_btn)

          change_slots_btn = TextButton(400,200, (0,128,128), f"# slots: {self.slots}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_slots_btn.onclick = self.slots_onclick
          self.add_button("slotup", change_slots_btn)
          
          change_colours_btn = TextButton(400,250, (0,128,128), f"# colours: {self.colours}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_colours_btn.onclick = self.colours_onclick
          self.add_button("colourup", change_colours_btn)

          change_guesses_btn = TextButton(400,300, (0,128,128), f"# guesses: {self.guesses}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_guesses_btn.onclick = self.guesses_onclick
          self.add_button("guessup", change_guesses_btn)

          duplicate_mode_btn = TextButton(400,350, (0,128,128), f"Duplicate mode: {self.duplicate_mode}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          duplicate_mode_btn.onclick = self.duplicate_mode_onclick
          self._btn_dict["duplicate"] = duplicate_mode_btn
          

     def start_onclick(self, game_controller):
          game_controller.message("start")

     def slots_onclick(self, game_controller):
          change_slots_btn = TextButton(400, 200, (0,128,128), f"# slots: {increment(4, 6, self.slots)}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_slots_btn.onclick = self.slots_onclick
          self._btn_dict["slotup"] = change_slots_btn
          self.slots = increment(4, 6, self.slots)

     def colours_onclick(self, game_controller):
          change_colours_btn = TextButton(400,250, (0,128,128), f"# colours: {increment(4, 16, self.colours)}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_colours_btn.onclick = self.colours_onclick
          self._btn_dict["colourup"] = change_colours_btn
          self.colours = increment(4, 16, self.colours)

     def guesses_onclick(self, game_controller):
          change_guesses_btn = TextButton(400,300, (0,128,128), f"# guesses: {increment(4, 12, self.guesses)}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          change_guesses_btn.onclick = self.guesses_onclick
          self._btn_dict["guessup"] = change_guesses_btn
          self.guesses = increment(4, 12, self.guesses)

     def duplicate_mode_onclick(self, game_controller):
          duplicate_mode_btn = TextButton(400,350, (0,128,128), f"Duplicate mode: {self.duplicate_mode}", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          duplicate_mode_btn.onclick = self.duplicate_mode_onclick
          self._btn_dict["duplicate"] = duplicate_mode_btn
          self.duplicate_mode = not self.duplicate_mode

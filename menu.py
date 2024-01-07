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
          self.guesses = 6
          self.colours = self.slots + 1
          self.duplicate_mode = False
          self.hard_mode = False

          text = "Mastermind"
          text_display = self.text_box_write(40, text)
          text_display.y = 30
          self._text_dict["terminal"] = text_display
          self._on_off_dict = {
               True: "on",
               False: "off"
          }

          start_btn = TextButton(400, 100, (0,0,0), "Start", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          start_btn.onclick = self.start_onclick
          self.add_button("start", start_btn)

          load_btn = TextButton(400, 200, (0,0,0), "Restore", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          load_btn.onclick = self.load_onclick
          self.add_button("load", load_btn)

          change_slots_btn = TextButton(400,250, (0,0,0), f"slots  {self.slots}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_slots_btn.onclick = self.slots_onclick
          change_slots_btn.change_onhover("-", "+")
          self.add_button("slotup", change_slots_btn)
          
          change_colours_btn = TextButton(400,300, (0,0,0), f"colours  {self.colours}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_colours_btn.onclick = self.colours_onclick
          change_colours_btn.change_onhover("-", "+")
          self.add_button("colourup", change_colours_btn)

          change_guesses_btn = TextButton(400,350, (0,0,0), f"guesses  {self.guesses}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_guesses_btn.onclick = self.guesses_onclick
          change_guesses_btn.change_onhover("-", "+")
          self.add_button("guessup", change_guesses_btn)

          duplicate_mode_btn = TextButton(400,400, (0,0,0), f"Duplicate mode  {self._on_off_dict[self.duplicate_mode]}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          duplicate_mode_btn.onclick = self.duplicate_mode_onclick
          self.add_button("duplicate", duplicate_mode_btn) 

          hard_mode_btn = TextButton(400,450, (0,0,0), f"Hard mode  {self._on_off_dict[self.hard_mode]}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          hard_mode_btn.onclick = self.hard_mode_onclick
          self.add_button("hard", hard_mode_btn)

     def start_onclick(self, game_controller):
          game_controller.message("start")

     def slots_onclick(self, game_controller):
          self.slots = increment(4, 6, self.slots)
          change_slots_btn = TextButton(400, 250, (0,0,0), f"slots  {self.slots}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_slots_btn.onclick = self.slots_onclick
          change_slots_btn.change_onhover("-", "+")
          self.add_button("slotup", change_slots_btn)
          if self.slots >= self.colours:
               self.colours = self.slots + 1
               change_colours_btn = TextButton(400,300, (0,0,0), f"colours  {self.colours}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
               change_colours_btn.onclick = self.colours_onclick
               change_colours_btn.change_onhover("-", "+")
               self.add_button("colourup", change_colours_btn)

     def colours_onclick(self,game_controller):
          self.colours = increment(self.slots + 1, 12, self.colours)
          change_colours_btn = TextButton(400,300, (0,0,0), f"colours  {self.colours}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_colours_btn.onclick = self.colours_onclick
          change_colours_btn.change_onhover("-", "+")
          self.add_button("colourup", change_colours_btn)
          

     def guesses_onclick(self, game_controller):
          self.guesses = increment(4, 8, self.guesses)
          change_guesses_btn = TextButton(400,350, (0,0,0), f"guesses  {self.guesses}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          change_guesses_btn.onclick = self.guesses_onclick
          change_guesses_btn.change_onhover("-", "+")
          self.add_button("guessup", change_guesses_btn)
          

     def duplicate_mode_onclick(self, game_controller):
          self.duplicate_mode = not self.duplicate_mode
          duplicate_mode_btn = TextButton(400,400, (0,0,0), f"Duplicate mode  {self._on_off_dict[self.duplicate_mode]}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          duplicate_mode_btn.onclick = self.duplicate_mode_onclick
          self.add_button("duplicate", duplicate_mode_btn) 
          
     def hard_mode_onclick(self, game_controller):
          self.hard_mode = not self.hard_mode
          hard_mode_btn = TextButton(400,450, (0,0,0), f"Hard mode  {self._on_off_dict[self.hard_mode]}", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          hard_mode_btn.onclick = self.hard_mode_onclick
          self.add_button("hard", hard_mode_btn) 
          
     def load_onclick(self, game_controller):
          game_controller.message("restore")
from screen import Screen
from rect_btn import RectButton
from text_btn import TextButton
from circle import Circle

class Board(Screen):
     def __init__(self, mastermind, pygame, screen):
          super().__init__(screen)

          self._pygame = pygame
          self._mastermind = mastermind
          self.counter = 0
          self.colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0)]
          self._colours = self.colours[:self._mastermind._options + 1]

          self._btn_width = round((400 - 25*(self._mastermind._slots - 1))/self._mastermind._slots)
          self._btn_height = round((400 - 10*(self._mastermind._guesses - 1))/self._mastermind._guesses)

          self.make_next_row()

          enter_btn = TextButton(700, 500, (0,128,128), "Enter", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          enter_btn.onclick = self.enter_onclick
          self.add_button("start", enter_btn)
          exit_btn = TextButton(50, 50, (0,128,128), "Return", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          exit_btn.onclick = self.exit_onclick

     ## answer work

     def draw_circles(self, colour_result):
          for i in range(0,4):
               x = 25 + 50*i
               y =  120 + self.counter*(self._btn_height+10)
               circle = Circle(x, y, colour_result[i], 10)
               self._item_dict[f"{x}"+f"{y}"] = circle

     ## row work
     def make_slot_btns(self, y): # makes the slots in a row
          for j in range(self._mastermind._slots):
               x = (200+(self._btn_width)/2) + j*(self._btn_width+25)

               btn = RectButton(x, y, self._colours, self._btn_width, self._btn_height, (128, 128, 128), self._pygame)
               btn.onclick = btn.colour_shift
               self.add_button(f"{self.counter}"+f"{j}", btn)
     
     def make_next_row(self):
          self.make_slot_btns(120 + self.counter*(self._btn_height+10))
          self.counter += 1
     
     def disable_row(self):
          for k in range(self._mastermind._slots):
               self._btn_dict[f"{self.counter - 1}" + f"{k}"].onclick = self.null_onclick

     ## button actions
     def enter_onclick(self, game_controller):
          if self.counter == self._mastermind._guesses:
               print(self._mastermind._answer)
               self.disable_row()
               self._btn_dict["start"].enter_onclick = self.null_onclick
          else:
               self.disable_row()
               self.make_next_row()
               colour_result = self._mastermind.answer_to_colour(self._btn_dict[f"{self.counter}" + f"{k}"] for k in range(self._mastermind._slots))
               self.draw_circles(colour_result)

     def null_onclick(self, game_controller):
          print("Can't click that!")
     
     def exit_onclick(self, game_controller):
          game_controller.message("exitboard")